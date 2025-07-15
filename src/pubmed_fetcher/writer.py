import csv
from typing import List, Dict


def write_csv(data: List[Dict[str, str]], filename: str) -> None:
    """Write article data to a CSV file."""
    if not data:
        print("No data to write.")
        return

    # Define the exact columns you want
    columns = [
        "PubmedID",
        "Title",
        "Publication Date",
        "Non-academic Author(s)",
        "Company Affiliation(s)",
        "Corresponding Author Email",
    ]

    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()
            writer.writerows(data)

        print(f"CSV file saved to {filename}")

    except Exception as e:
        print(f"Error writing to CSV: {e}")
