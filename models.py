from datetime import datetime
from pydantic import BaseModel, Field, field_validator

class Weather_report(BaseModel):
    city: str
    country: str
    temperature: float = Field(ge=-90.0,le=60.0)
    humidity:int = Field(le=100, ge=0)
    recorded_at: datetime
    
    @field_validator("country")
    @classmethod
    
    def change_to_upper(cls,v:str):
        return v.upper() 