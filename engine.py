import json
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from models import Weather_report
from datetime import datetime

class DataEngine:
    def __init__(self):
        self.base_url = "https://wttr.in/{}?format=j1" #real-world open source weather service
        
    def fetch_raw_data(self, city:str):
        url = self.base_url.format(city)
        with urllib.request.urlopen(url) as response:
            return json.loads(response.read().decode())
        
    def process_city(self, city):
        try:
            raw_data = self.fetch_raw_data(city)
            area = raw_data["nearest_area"][0]
            condition = raw_data["current_condition"][0]
            
            time_str = condition.get("localObsDateTime") or condition.get("localObsTime") or condition.get("observation_time")
            
            if time_str and len(time_str) <= 8:
                today_date = datetime.now().strftime("%Y-%m-%d")
                full_time_str = f"{today_date} {time_str}"
                timestamp = datetime.strptime(full_time_str, "%Y-%m-%d %I:%M %p")
            else:
                try:
                    timestamp = datetime.fromisoformat(time_str) if time_str else datetime.now()
                except ValueError:
                    timestamp = datetime.now()
                
            cleaned_payload={
                "city":area["areaName"][0]["value"],
                "country": area["country"][0]["value"],
                "temperature": condition["temp_C"],
                "humidity": condition["humidity"],
                "recorded_at": timestamp
            }
            return Weather_report(**cleaned_payload)
        except Exception as e:
            print(f"Error processing metrics: {e}")
            return None
        
    def process_all_cities(self, cities):
        with ThreadPoolExecutor(max_workers=10) as executors:
            result = executors.map(self.process_city,cities)
            return [report for report in result if report is not None]