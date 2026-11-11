import pandas as pd
import matplotlib.pyplot as plt

# Load category expression summary
df = pd.read_csv(
    "data/functional_category_expression_summary.csv"
)

# Sort categories by EV-WP difference
df = df.sort_values("Mean_EV_minus_WP")

# Create figure
plt.figure(figsize=(11, 7))

plt.barh(
    df["Analysis_Category"],
    df["Mean_EV_minus_WP"]
)

# Add zero reference line
plt.axvline(x=0, linestyle="--", linewidth=1)

# Labels and title
plt.xlabel("Mean expression difference (EV - WP)")
plt.ylabel("Functional category")

plt.title(
    "EV versus WP Expression Differences by Functional Category"
)

plt.tight_layout()

# Save figure
plt.savefig(
    "figures/functional_category_expression_difference.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Functional category difference plot saved successfully!")