import gzip
import re
from pathlib import Path

# Project folders
DATA_DIR = Path("data")
INPUT_FILE = DATA_DIR / "GSE241277_family.soft"
OUTPUT_FILE = DATA_DIR / "sample_metadata.csv"

samples = []
current_sample = None

# Read the GEO SOFT file
with open(INPUT_FILE, "r", encoding="utf-8") as file:

    for line in file:

        line = line.strip()

        if line.startswith("^SAMPLE"):
            if current_sample:
                samples.append(current_sample)

            current_sample = {
                "GSM": line.split("=")[1].strip(),
                "title": "",
                "characteristics": []
            }

        elif current_sample:

            if line.startswith("!Sample_title"):
                current_sample["title"] = line.split("=", 1)[1].strip()

            elif line.startswith("!Sample_characteristics_ch1"):
                value = line.split("=", 1)[1].strip()
                current_sample["characteristics"].append(value)

    if current_sample:
        samples.append(current_sample)

# Save metadata
import csv

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow(["GSM", "Title", "Characteristics"])

    for sample in samples:
        writer.writerow([
            sample["GSM"],
            sample["title"],
            "; ".join(sample["characteristics"])
        ])

print("Metadata extraction complete!")
print("Samples found:", len(samples))
print("Saved to:", OUTPUT_FILE)