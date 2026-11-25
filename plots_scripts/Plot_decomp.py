import matplotlib.pyplot as plt
import numpy as np

def plot_decomp(df_decomp):
    # 1. Select the columns you want to plot
    cols_to_plot = ["Electrostatic", "van der Waals", "TOTAL"]
    
    # Create a new DataFrame with just those columns
    plot_df = df_decomp.iloc[:-1].set_index("Residue")[cols_to_plot]
    #plot_df = df_decomp.set_index("Residue")[cols_to_plot]
    
    # 2. Set up the plot
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # 3. Plot the grouped bar chart
    # pandas automatically handles grouping and the x-axis labels
    plot_df.plot(
        kind="bar",
        ax=ax,
        width=0.8,
        color=["#d62728", "#1f77b4", "#2ca02c"], # Red (Elec), Blue (vdW), Green (Total)
        edgecolor="black",
        linewidth=0.5
    )
    
    # 4. Formatting
    ax.axhline(0, color="black", linewidth=0.8)
    ax.set_title("Per-Residue Energy Decomposition (Total)", fontsize=16, pad=15, fontweight="bold")
    ax.set_xlabel("Residue", fontsize=16, fontweight="bold")
    ax.set_ylabel("Energy (kcal/mol)", fontsize=16, fontweight="bold")
    
    # Rotate x-axis labels for readability
    plt.xticks(rotation=45, ha="right", fontsize=12, fontweight="bold")
    
    # Add gridlines for easier reading
    ax.grid(axis="y", linestyle="--", alpha=0.5)
    
    # Add a legend
    ax.legend(title="Energy Component", loc="upper right")
    
    plt.tight_layout()
    plt.show()