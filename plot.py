from pathlib import Path

import matplotlib

# Use a noninteractive backend suitable for GitHub Actions.
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


def main():
    """Plot y = x^2 on the interval [-2, 2] and save it as f1.png."""
    x = np.linspace(-2, 2, 401)
    y = x**2

    figure, axis = plt.subplots(figsize=(7, 5))

    axis.plot(x, y, color="blue", linewidth=2, label=r"$y=x^2$")
    axis.axhline(0, color="black", linewidth=0.8)
    axis.axvline(0, color="black", linewidth=0.8)
    axis.set_xlim(-2, 2)
    axis.set_xlabel("x")
    axis.set_ylabel("y")
    axis.set_title(r"Plot of $y=x^2$")
    axis.grid(True, alpha=0.3)
    axis.legend()

    output_file = Path(__file__).resolve().parent / "f1.png"
    figure.tight_layout()
    figure.savefig(output_file, dpi=200)
    plt.close(figure)

    print(f"Saved plot to {output_file}")


if __name__ == "__main__":
    main()
