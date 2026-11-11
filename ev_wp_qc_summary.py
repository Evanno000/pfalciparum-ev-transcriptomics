import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
REPORT_DIR = BASE_DIR / "report"

REPORT_DIR.mkdir(exist_ok=True)

summary = pd.read_csv(
    DATA_DIR / "sample_expression_summary.csv"
)

metadata = pd.read_csv(
    DATA_DIR / "sample_mapping.csv"
)

combined = summary.merge(
    metadata[["Expression_Column", "Treatment_Type"]],
    left_on="Sample",
    right_on="Expression_Column"
)

result = combined.groupby("Treatment_Type")[
    ["Mean", "Median", "Standard_Deviation"]
].agg(["mean", "median", "min", "max"]).round(3)

output = REPORT_DIR / "ev_wp_qc_summary.csv"
result.to_csv(output)

print(result)
print("\nSaved:", output)