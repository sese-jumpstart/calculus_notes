
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

    figure, axis = plt.su**lots(figsize=(7, 5))

    axis.pl**(x, y, color="blue", linewidth=2,**abel=r"$y=x^2$")
    axis.axhline**, color="black", linewidth=0.8)
 ** axis.axvline(0, color="black", l**ewidth=0.8)
    axis.set_xlim(-2,**)
    axis.set_xlabel("x")
    ax**.set_ylabel("y")
    axis.set_tit**(r"Plot of $y=x^2$")
    axis.gri**True, alpha=0.3)
    axis.legend(**
    output_file = Path(__file__)**esolve().parent / "f1.png"
    fi**re.tight_layout()
    figure.save**g(output_file, dpi=200)
    plt.c**se(figure)

    print(f"Saved plo**to {output_file}")


if __name__ ** "__main__":
    main()
