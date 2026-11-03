"""Plot individual training-error histories exported from Weights & Biases.

Run from the repository root with:
    uv run python papers/2015-deep-residual-learning/results/plot_training_error.py
"""

import csv
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.ticker import FuncFormatter

RESULTS_DIRECTORY = Path(__file__).resolve().parent
CSV_PATH = RESULTS_DIRECTORY / "wandb-training-error.csv"
SEEDS = (147, 148, 149, 150, 151)
MODELS = ("PlainNet-20", "PlainNet-56", "ResNet-20", "ResNet-56")
# Use the same seed-to-shade mapping in both network families.
COLORS = {
    20: ("#64A7D3", "#277FB8", "#185587", "#299C99", "#126D67"),
    56: ("#ECA052", "#DD792B", "#C65620", "#B43F3F", "#7F283A"),
}


def main() -> None:
    """Validate the CSV and save two figures without smoothing or aggregation."""
    with CSV_PATH.open(newline="") as handle:
        reader = csv.DictReader(handle)
        columns = reader.fieldnames or []
        rows = list(reader)

    iterations = [int(row["iteration"]) for row in rows]
    if iterations != list(range(100, 64_001, 100)):
        raise ValueError("Expected 640 points at 100-iteration intervals.")

    series = {}
    expected_columns = {f"{model}-seed-{seed} - train/error" for model in MODELS for seed in SEEDS}
    if {column for column in columns if column.endswith(" - train/error")} != expected_columns:
        raise ValueError("Expected exactly four models with five seeds each.")
    for column in expected_columns:
        values = [float(row[column]) for row in rows]
        if not all(math.isfinite(value) and 0 <= value <= 100 for value in values):
            raise ValueError(f"Invalid training errors in {column}.")
        for suffix in ("__MIN", "__MAX"):
            if [float(row[column + suffix]) for row in rows] != values:
                raise ValueError(f"{column + suffix} differs from the base series; inspect aggregation.")
        series[column] = values

    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 11,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.labelcolor": "#333333",
            "axes.edgecolor": "#BBBBBB",
            "xtick.color": "#555555",
            "ytick.color": "#555555",
            "savefig.facecolor": "white",
        }
    )
    for family, title in (("PlainNet", "Plain networks"), ("ResNet", "Residual networks")):
        fig = plt.figure(figsize=(12.5, 7.7))
        axis = fig.add_axes((0.085, 0.245, 0.875, 0.635))
        fig.text(0.085, 0.94, title, fontsize=18, fontweight="bold")
        axis.set(
            xlim=(0, 64_000), ylim=(0, 100), xlabel="Training iteration", ylabel="Training classification error (%)"
        )
        axis.set_xticks([0, 16_000, 32_000, 48_000, 64_000])
        axis.xaxis.set_major_formatter(FuncFormatter(lambda value, _: f"{value / 1000:g}k" if value else "0"))
        axis.grid(axis="y", color="#E5E7EB", linewidth=0.7)
        axis.set_axisbelow(True)
        for milestone in (32_000, 48_000):
            axis.axvline(milestone, color="#AAAAAA", linestyle="--", linewidth=0.8, zorder=0)

        inset = axis.inset_axes([0.53, 0.43, 0.43, 0.37])
        inset.set(xlim=(48_000, 64_000), ylim=(0, 10))
        inset.set_title("Final 16,000 iterations", fontsize=10, loc="left", pad=7)
        inset.set_xticks([48_000, 56_000, 64_000], ["48k", "56k", "64k"])
        inset.set_yticks([0, 5, 10], ["0%", "5%", "10%"])
        inset.tick_params(labelsize=9)
        inset.grid(axis="y", color="#E5E7EB", linewidth=0.6)
        inset.set_axisbelow(True)

        handles = []
        for depth in (20, 56):
            model = f"{family}-{depth}"
            for seed, color in zip(SEEDS, COLORS[depth], strict=True):
                handles.append(Line2D([], [], color=color, linewidth=2, label=f"{model}, seed {seed}"))
                values = series[f"{model}-seed-{seed} - train/error"]
                axis.plot(iterations, values, color=color, alpha=0.9, linewidth=0.85)
                inset.plot(iterations, values, color=color, alpha=0.9, linewidth=0.85)
        # Matplotlib fills legend columns first; keep each depth on its own row.
        legend_handles = [handle for pair in zip(handles[:5], handles[5:], strict=True) for handle in pair]
        fig.legend(
            handles=legend_handles,
            loc="lower left",
            bbox_to_anchor=(0.085, 0.09),
            ncol=5,
            frameon=False,
            fontsize=9,
            handlelength=2,
            columnspacing=1.5,
            labelspacing=1.2,
            borderaxespad=0,
        )
        fig.text(
            0.085,
            0.035,
            "Five seeds per model; each line is one run. No smoothing. Dashed lines mark learning-rate reductions.",
            fontsize=9,
            color="#555555",
        )
        output_path = RESULTS_DIRECTORY / f"{family.lower()}-training-error.png"
        fig.savefig(output_path, dpi=240)
        plt.close(fig)
        print(output_path)


if __name__ == "__main__":
    main()
