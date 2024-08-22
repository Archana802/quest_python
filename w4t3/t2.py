# DateLibrary.py

from datetime import datetime

def todays_date():
    return datetime.now().strftime("%d-%m-%Y")
