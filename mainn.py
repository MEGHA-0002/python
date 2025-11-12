# main.py

import json
from datetime import datetime
from tracker import create_record

# Create at least 3 records
records = [
    create_record("Berlin", "Visited the Brandenburg Gate.", "19-06-2022"),
    create_record("Cape Town", "Enjoyed Table Mountain.", "05-11-2023"),
    create_record("Kyoto", "Cherry blossoms everywhere!", "12-04-2024"),
]

# Format the dates
for record in records:
    date_obj = datetime.strptime(record["date"], "%d-%m-%Y")
    record["date"] = date_obj.strftime("%B %d, %Y")

# Convert to JSON string
json_str = json.dumps(records, indent=2)
print("JSON output:")
print(json_str)

# Parse JSON back to Python object and print each record
print("\nParsed records:")
parsed_records = json.loads(json_str)
for rec in parsed_records:
    # Print each record on a separate line
    print(rec)
