from engine import DataEngine

if __name__=="__main__":
    print("Initializing Global Weather Engine")
    engine  = DataEngine()
    
    target_cities = ['Paris','Tokyo','New+York','London','Delhi']
    
    validated_reports = engine.process_all_cities(target_cities)
    for report in validated_reports:
        print(f"city: {report.city},{report.country}")
        print(f"Temp:{report.temperature}°C | Humidity:{report.humidity}")
        print(f"Tracked at {report.recorded_at}")