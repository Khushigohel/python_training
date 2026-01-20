##### Load & Validate Data  #######
import os
import json
from datetime import datetime

BASE_DIR = os.path.dirname(__file__)
file_path=os.path.join(BASE_DIR,'weather_data.json')
file_error=os.path.join(BASE_DIR,'errors.log')

def load_date(file_path=file_path):
    records=[]
    error=[]
    
    with open(file_path,'r') as read_json_data:
        data=json.load(read_json_data)   # load(convert json into pthon object )
        
    for result in data:
        #print(result)
        try:
            result["timestamp"]=datetime.fromisoformat(result["timestamp"])
            result["temperature"]=float(result["temperature"])
            result["rainfall"]=float(result['rainfall'])
            result["humidity"]=float(result["humidity"])
            records.append(result)
            
        except Exception as e:
            error.append(f"Invalid  record{result} - {e}")
    
    with open(file_error,'w') as write_error:
        for err in error:
            write_error.write(err + "\n ")
    return records
            
#res=load_date(file_path)
#print(res)
#print(data)

def get_daily_avg_temperature(readings):
    temp_dict={}
    for r in readings:
        date_str = r.timestamp.date().isoformat()
        
        if r.station_id not in temp_dict:
            temp_dict[r.station_id] = {}
        
        if date_str not in temp_dict[r.station_id]:
            temp_dict[r.station_id][date_str] = []
        
        temp_dict[r.station_id][date_str].append(r.temperature)
        
   #average count     
    avg_date={}
    for station in temp_dict:
        avg_date[station] = {}
        for date in temp_dict[station]:
            temps = temp_dict[station][date]
            avg_date[station][date] = sum(temps) / len(temps)

    return avg_date

def get_daily_rainfall(readings):
    rain_data = {} 

    for r in readings:
        date_str = r.timestamp.date().isoformat()

        if r.station_id not in rain_data:
            rain_data[r.station_id] = {}
        
        if date_str not in rain_data[r.station_id]:
            rain_data[r.station_id][date_str] = 0.0
        
        rain_data[r.station_id][date_str] += r.rainfall

    return rain_data
