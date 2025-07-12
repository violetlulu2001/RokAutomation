from datetime import datetime

def get_datetime_format() -> str:
    now = datetime.now()
    return now.strftime("%Y%m%d_%H%M%S")

