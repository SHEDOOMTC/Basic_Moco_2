import re
import pandas as pd

def process_mmgbsa(filepath):
    # Read the file into a list of lines so we can scan from the bottom upward
    with open(filepath, "r", encoding="cp1252") as f:
        lines = f.read().splitlines()

    # Work backward until the last "Differences (Complex - Receptor - Ligand):" block
    start = None
    for i in range(len(lines) - 1, -1, -1):
        if "Differences (Complex - Receptor - Ligand):" in lines[i]:
            start = i
            break

    if start is None:
        raise ValueError("Could not find the final Differences section")

    # Keep only this section, stopping before the final entropy note
    section = []
    for line in lines[start:]:
        if line.startswith("Using Normal Mode Entropy Approximation"):
            break
        section.append(line)

    text = "\n".join(section)

    # Extract the energy table that follows the header
    header = "Energy Component            Average              Std. Dev.   Std. Err. of Mean"
    start_table = text.find(header)
    if start_table == -1:
        raise ValueError("Could not find the energy table header")

    table_text = text[start_table:]

    rows = []
    for line in table_text.splitlines():
        s = line.strip()
        if not s or "---" in s or "Energy Component" in s:
            continue

        parts = re.split(r"\s{2,}", s)
        if len(parts) < 4:
            continue

        component, avg, std_dev, sem = parts[:4]
        rows.append({
            "Component": component,
            "Average": float(avg),
            "Std. Dev.": float(std_dev),
            "Std. Err. of Mean": float(sem),
        })

    # Build a DataFrame and print it
    df_energy = pd.DataFrame(rows).set_index("Component")
    print(df_energy)

    # Get the binding free energy from the last section
    delta_total = df_energy.loc["DELTA TOTAL", "Average"]
    print(f"\nDELTA TOTAL = {delta_total}")
    return df_energy
