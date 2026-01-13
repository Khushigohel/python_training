# Weather Alert & Summary System

This project processes daily weather readings from JSON data, generates alerts, calculates daily statistics, and exports a summary report.

---

##  Project Structure

weather_assignment/
│── weather_data.json  
│── models.py  
│── processor.py  
│── alerts.py  
│── main.py  
│── summary.json  
│── errors.log  
│── README.md  

---

## 🧩 Features / Tasks Completed

1. **Load & Validate Data**
   - Reads `weather_data.json`
   - Converts:
     - timestamp → datetime
     - temperature, rainfall, humidity → float
   - Invalid records are skipped and logged into `errors.log`

2. **WeatherReading Class (OOP)**
   - Attributes:
     - station_id, timestamp, temperature, rainfall, humidity
   - Methods:
     - `is_hot(threshold=40)`
     - `is_heavy_rain(threshold=50)`

3. **Daily Aggregations**
   - Computes:
     - Daily average temperature
     - Daily total rainfall

4. **Alert Generation**
   - Alerts:
     - `HEAT_ALERT`: temperature > 40°C
     - `HEAVY_RAIN_ALERT`: rainfall > 100 mm per day

5. **Summary Export**
   - Generates `summary.json` output:
   ```json
   {
     "daily_summary": {
       "ST001": {
         "2024-01-05": {
           "avg_temperature": 36.8,
           "total_rainfall": 12,
           "alerts": ["HEAT_ALERT"]
         }
       }
     }
   }
