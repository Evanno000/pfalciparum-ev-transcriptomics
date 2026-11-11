import csv
from pathlib import Path

input_file = Path("data/sample_metadata.csv")
output_file = Path("data/organised_metadata.csv")

organised_samples = []

with open(input_file, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        characteristics = {}

        for item in row["Characteristics"].split(";"):
            if ":" in item:
                key, value = item.split(":", 1)
                characteristics[key.strip()] = value.strip()

        treatment = characteristics.get("treatment", "")

        parts = treatment.split("_")

        treatment_type = parts[0] if len(parts) >= 2 else ""
        time_point = parts[1] if len(parts) >= 2 else ""

        organised_samples.append({
            "GSM": row["GSM"],
            "Title": row["Title"],
            "Cell_Line": characteristics.get("cell line", ""),
            "Genotype": characteristics.get("genotype", ""),
            "Treatment": treatment,
            "Treatment_Type": treatment_type,
            "Time_Point": time_point
        })

with open(output_file, "w", newline="", encoding="utf-8") as file:
    columns = [
        "GSM", "Title", "Cell_Line", "Genotype",
        "Treatment", "Treatment_Type", "Time_Point"
    ]

    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(organised_samples)

print("Metadata organisation complete!")
print("Total samples:", len(organised_samples))
print("Saved to:", output_file)