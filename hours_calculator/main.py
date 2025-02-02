from typing import Annotated
from fastapi import FastAPI, Path
from pydantic import BaseModel
from datetime import datetime

from calendar import Calendar

app = FastAPI(root_path="/api")
class Hours(BaseModel):
    peak_hour: int
    non_peak_hour: int

# should be in a database but storing it here for simplicity
non_peak_hours = [20,21,22,23,0,1,2,3,4,5]
non_peak_days = ["Saturday","Sunday"]

@app.get("/")
def check_health():
    return "success"

@app.get("/hours/{month}/{year}")
def calculate_hours(
    month: Annotated[int, Path(title="Month in numeric format", ge=1, le=12)], 
    year: Annotated[int, Path(title="Year in YYYY format", ge=1800, le=datetime.now().year)]) -> Hours:
    """
     Return peak and non-peak hours for a given month and year
    """
    total_peak_hours = 0
    total_non_peak_hours = 0
    max_operating_hours_count = 24
    peak_hours_count = max_operating_hours_count - len(non_peak_hours)

    calendarObj = Calendar()
    # parse and iterate through each day
    for day in calendarObj.itermonthdates(year, month):
        if day.month == month: # itermonthdates includes days before and after month to complete a week, must do a month check
            if day.strftime("%A") in non_peak_days: # if day is a non-peak day, add to non-peak hours
                total_non_peak_hours += max_operating_hours_count
            else: # if day is a peak day, add peak hours and non peak hours
                total_peak_hours += peak_hours_count
                total_non_peak_hours += max_operating_hours_count - peak_hours_count
    
    return Hours(peak_hour = total_peak_hours, non_peak_hour = total_non_peak_hours)