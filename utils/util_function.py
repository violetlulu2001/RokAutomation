from datetime import datetime
import random
from utils.reader_json import fiddle

def get_datetime_format() -> str:
    now = datetime.now()
    return now.strftime("%Y%m%d_%H%M%S%f")

def default_text(name_script:str, name:str , x_coord: str, y_coord: str):
    return f"[{get_datetime_format().split("_")[-1]}] -  {name_script}.py | Press {name} on coordinate X:{x_coord}, Y:{y_coord}\n"


def get_random_fiddle_stick():
    return random.choice(fiddle['Fiddlestick'])
