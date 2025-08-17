# Marimo notebook: Interactive Relationship Explorer
# Author contact: 23f2002133@ds.study.iitm.ac.in
# 23f2002133@ds.study.iitm.ac.in
import marimo

__generated_with = "0.8.15"
app = marimo.App()

# ──────────────────────────────────────────────────────────────────────────────
# Cell 1: Imports and setup
# Data flow note:
#   - Downstream cells depend on numpy/pandas/matplotlib imported here.
#   - This cell has no upstream dependencies.
# ──────────────────────────────────────────────────────────────────────────────
@app.cell
def __(mo):
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    # Make plots crisp in retina displays
    plt.rcParams["figure.dpi"] = 120
    plt.rcParams["figure.figsize"] = (5, 3.2)
    mo.md("# Interactive data relationship notebook").display()
    mo.md(
        "Use the slider to control noise in a simple linear model and observe how "
        "the scatter plot and correlation respond. This notebook is self-documenting: "
        "each cell includes comments describing upstream and downstream dependencies."
    ).display()
    return np, pd, plt

# ──────────────────────────────────────────────────────────────────────────────
# Cell 2: Interactive control (slider)
# Data flow note:
#   - Outputs: noise_slider (widget), sigma (current value)
#   - Downstream: data generation (Cell 3), narrative markdown (Cell 6), annotations (Cell 7)
# ──────────────────────────────────────────────────────────────────────────────
@app.cell
def __(mo):
    noise_slider = mo.ui.slider(
        start=0.0, stop=2.0, step=0.1, value=0.5, label="Noise level (σ)"
    )
    sigma = noise_slider.value
    mo.hstack([mo.md("### Controls"), noise_slider]).display()
    return noise_slider, sigma

# ──────────────────────────────────────────────────────────────────────────────
# Cell 3: Data generation driven by the slider
# Data flow note:
#   - Upstream: sigma from Cell 2
#   - Outputs: df (DataFrame), x, y
#   - Downstream: correlation (Cell 4), plotting (Cell 5), narrative (Cell 6)
# Model:
#   y = 2x + ε, where ε ~ Normal(0, σ), with x ~ Uniform(0, 1)
# ──────────────────────────────────────────────────────────────────────────────
@app.cell
def __(np, pd, sigma):
    rng = np.random.default_rng(42)  # deterministic for demo
    n = 200
    x = rng.uniform(0, 1, size=n)
    eps = rng.normal(0, sigma, size=n)
    y = 2 * x + eps
    df = pd.DataFrame({"x": x, "y": y})
    return df, x, y

# ──────────────────────────────────────────────────────────────────────────────
# Cell 4: Summary statistics derived from data
# Data flow note:
#   - Upstream: df from Cell 3
#   - Outputs: r (Pearson correlation)
#   - Downstream: narrative (Cell 6), annotations (Cell 7)
# ──────────────────────────────────────────────────────────────────────────────
@app.cell
def __(df):
    r = df["x"].corr(df["y"])
    return (r,)

# ──────────────────────────────────────────────────────────────────────────────
# Cell 5: Visualization
# Data flow note:
#   - Upstream: df from Cell 3
#   - Uses: matplotlib from Cell 1
#   - Downstream: None (purely visual side-effect)
# ──────────────────────────────────────────────────────────────────────────────
@app.cell
def __(df, plt):
    fig, ax = plt.subplots()
    ax.scatter(df["x"], df["y"], s=14, alpha=0.8)
    ax.set_title("Scatter of y vs. x")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True, linestyle="--", linewidth=0.5, alpha=0.6)
    fig  # returning the figure displays it
    return (fig,)

# ──────────────────────────────────────────────────────────────────────────────
# Cell 6: Dynamic, self-updating markdown
# Data flow note:
#   - Upstream: sigma (Cell 2), r (Cell 4)
#   - Downstream: None
# Behavior:
#   - Text recomputes automatically when slider moves.
# ──────────────────────────────────────────────────────────────────────────────
@app.cell
def __(mo, r, sigma):
    trend = (
        "strong" if abs(r) > 0.8 else
        "moderate" if abs(r) > 0.5 else
        "weak" if abs(r) > 0.3 else
        "very weak"
    )
    mo.md(f"""
### Findings
- Current noise level **σ = {sigma:.1f}**
- Pearson correlation **r = {r:.3f}** → *{trend}* linear relationship
- As σ increases, points spread further from the line *y = 2x*, reducing |r|.
""").display()
    return trend

# ──────────────────────────────────────────────────────────────────────────────
# Cell 7: Lightweight annotation & provenance
# Data flow note:
#   - Upstream: noise_slider (Cell 2), r (Cell 4)
#   - Downstream: None
# Purpose:
#   - Shows live values without recomputation; demonstrates widget state usage.
# ──────────────────────────────────────────────────────────────────────────────
@app.cell
def __(mo, noise_slider, r):
    mo.hstack([
        mo.callout(
            f"Live widget value σ = {float(noise_slider.value):.1f}",
            kind="info"
        ),
        mo.callout(
            f"Live correlation r = {float(r):.3f}",
            kind="success"
        )
    ]).display()

# Entry point
if __name__ == "__main__":
    app.run()
