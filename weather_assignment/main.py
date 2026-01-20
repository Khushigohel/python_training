from models import WeatherReading
from processor import load_date,get_daily_avg_temperature,get_daily_rainfall
from alerts import generate_alerts
import json
import os

BASE_DIR = os.path.dirname(__file__)
file_path=os.path.join(BASE_DIR,'summary.json')

## 1.load date task 1
result=load_date()
#print(result)

## Convert dicts - WeatherReading objects
readings = [WeatherReading(**rec) for rec in result]

#Task 2
for r in readings:
    if r.is_hot():
        print(f"{r.station_id} is HOT at {r.timestamp}")
    if r.is_heavy_rain():
        print(f"{r.station_id} is heavy rain at {r.timestamp}")
        
### task 3
ave_temperature= get_daily_avg_temperature(readings)
daily_rainfall=get_daily_rainfall(readings)

# print("Average Temp:", ave_temperature)
# print("Total Rainfall:", daily_rainfall)

## task 4
res=generate_alerts(readings)
#print(dict(res))


## task 5
summary = {
    "daily_summary": {}
}

for station in ave_temperature:
    summary["daily_summary"][station] = {}
    for date in ave_temperature[station]:
        summary["daily_summary"][station][date] = {
            "avg_temperature": round(ave_temperature[station][date], 2),
            "total_rainfall": daily_rainfall[station][date],
            "alerts": res.get(station, {}).get(date, [])
        }

with open(file_path, "w") as f:
    json.dump(summary, f, indent=4)

print("Summary saved to summary.json")