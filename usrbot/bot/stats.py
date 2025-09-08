import os
import shlex, subprocess
from pathlib import Path

import time
import schedule

main_dir = Path(__file__).parent

scripts = main_dir / 'scripts'

bat =       (scripts / 'get_bat')
bright =    (scripts / 'get_bright')
mem =       (scripts / 'get_mem')
set_brigh = (scripts / 'set_bright')





def get_bat() -> str:
    battery = ['bash', bat]

    try:
        get_battery = subprocess.check_output(battery, text=True)
        return get_battery
    except:
        return 'None'
    
    



def get_mem() -> str:
    """
    Purpose: 
    """
    
    args = ['bash', mem]

    try:
        process = subprocess.check_output(args, text=True)
        return process
    except:
        return 'None'


def get_bright() -> str:
    args = ['bash', bright]

    try:
        process = subprocess.check_output(args, text=True)
        return process
    except:
        return 'None'




def set_bright(a: str):
    args = ['bash', set_brigh, a]
    print(f"{__name__}: {args}")
    try:
        subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return get_bright()
    except:
        return 'None'


def get_full():
    bat = get_bat()
    mem = get_mem()
    brght = get_bright()

    msg = f"""
    battery:```bash
    \n{bat}```
    \nmem:```bash
    \n{mem}```
    \nbright:```bash
    \n{brght}```

    """

    return msg



# schedule.every(10).minutes.do(bat_alarm)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
