from typing import Annotated
from fastapi import FastAPI, Path
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(root_path="/api")
class Hours(BaseModel):
    peak_hour: int
    non_peak_hour: int

# should be in a database but storing it here for simplicity
non_peak_hours = [21,22,23,0,1,2,3,4,5]
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
    # get number of days in a month
    # parse and iterate through each day
    # if day is a non-peak day, add to non-peak hours (24)
    # if day is a peak day, add peak hours and non peak hours

    return Hours(peak_hour=0, non_peak_hour=0)