import re
import pandas as pd

def process_decomp(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    # 1. Find the "Total Energy Decomposition:" header
    start = None
    for i, line in enumerate(lines):
        if line.strip() == "Total Energy Decomposition:":
            start = i
            break

    if start is None:
        raise ValueError("Could not find the 'Total Energy Decomposition' section.")

    # 2. Find the actual column headers (the line starting with "Residue |")
    header_idx = None
    for i in range(start, len(lines)):
        if lines[i].startswith("Residue |"):
            header_idx = i
            break
            
    if header_idx is None:
        raise ValueError("Could not find the column headers in the decomposition section.")

    # 3. Read the data lines
    rows = []
    for line in lines[header_idx + 2:]: # Start after header and the dashed line
        s = line.strip()
        
        # Stop if we hit the end of this table (blank line or next section)
        if not s or s.startswith("---") or "Decomposition:" in s:
            break
            
        parts = [p.strip() for p in s.split("|")]
        
        if len(parts) < 8:
            continue
            
        residue = parts[0]
        location = parts[1]
        
        # Helper to extract the first number (the mean) from strings like "-1.376 +/-  0.704"
        def extract_mean(val_str):
            try:
                return float(val_str.split("+/-")[0].strip())
            except ValueError:
                return None
                
        rows.append({
            "Residue": residue,
            "Location": location,
            "Internal": extract_mean(parts[2]),
            "van der Waals": extract_mean(parts[3]),
            "Electrostatic": extract_mean(parts[4]),
            "Polar Solvation": extract_mean(parts[5]),
            "Non-Polar Solv.": extract_mean(parts[6]),
            "TOTAL": extract_mean(parts[7])
        })

    # 4. Create the DataFrame
    df_decomp = pd.DataFrame(rows).dropna(how="all")
    
    print(df_decomp)
    return df_decomp