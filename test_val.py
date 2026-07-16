from datetime import datetime
import pytest
from pydantic import ValidationError
from models import Weather_report

def test_data_validity():
    payload={
        "city":"Paris",
        "country":"France",
        "temperature":18.5,
        "humidity":65,
        "recorded_at": datetime.now()
    }
    
    report = Weather_report(**payload)
    
def test_invalid_temperature():
    with pytest.raises(ValidationError):
        Weather_report(
            city="Paris",
            country="france",
            temperature=150.5,
            humidity=10,
            recorded_at=datetime.now()
        )

def test_invalid_humidity():
    with pytest.raises(ValidationError):
        Weather_report(
            city="Sahara",
            country="Egypt",
            temperature=12.0,
            humidity=-5,
            recorded_at=datetime.now()
        )