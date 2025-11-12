import json
from datetime import datetime
from tripdata import get_trips

trips_list = get_trips()
formatted_trips = []

for trip in trips_list:
    # Convert date string to date object
    date_obj = datetime.strptime(trip["date"], "%d-%m-%Y")
    # Format the date as "Month Day, Year"
    formatted_date = date_obj.strftime("%B %d, %Y")
    # Build new trip dictionary with formatted date
    formatted_trips.append({
        "city": trip["city"],
        "date": formatted_date,
        "comment": trip["comment"]
    })

# Convert to JSON string and print
trips_json = json.dumps(formatted_trips, indent=2)
print(trips_json)
