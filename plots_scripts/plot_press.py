import matplotlib.pyplot as plt

def plot_press(filename="step_press.dat"):
    steps = []
    energies = []

    with open(filename) as f:
        for line in f:
            if "--" in line:   # skip separator lines
                continue
            parts = line.split()
            if len(parts) >= 2:
                steps.append(int(parts[0]))
                energies.append(float(parts[1]))

    # Plot
    plt.figure(figsize=(8,5))
    plt.plot(steps, energies, marker='o', linestyle='-')
    plt.xlabel("Step")
    plt.ylabel("Pressure (atm)")
    plt.title("NPT Equilibration")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Run automatically if executed directly
if __name__ == "__main__":
    plot_press()

