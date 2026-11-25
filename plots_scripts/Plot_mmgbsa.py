import matplotlib.pyplot as plt


import matplotlib.pyplot as plt

def plot_mmgbsa(df_energy):
    # Bar plot of each MM/GBSA energy component using SEM as error bars
    plt.figure(figsize=(10, 6))
    ax = plt.gca()

    ax.bar(
        df_energy.index,
        df_energy["Average"],
        yerr=df_energy["Std. Err. of Mean"],
        capsize=4,
        color="steelblue",
        edgecolor="black"
    )

    ax.axhline(0, color="black", linewidth=0.8)
    ax.set_title("MM/GBSA Energy Components", fontsize=14, fontweight="bold")
    ax.set_xlabel("Energy Component", fontsize=12, fontweight="bold")
    ax.set_ylabel("Average Energy (kcal/mol)", fontsize=12, fontweight="bold")
    ax.grid(axis="y", linestyle="--", alpha=0.4)
    plt.xticks(rotation=45, ha="right", fontsize=10, fontweight="bold")
    plt.yticks(fontsize=10, fontweight="bold")
    plt.tight_layout()
    plt.show()
