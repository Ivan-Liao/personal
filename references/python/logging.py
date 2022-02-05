import datetime as dt
import os
import logging
logging.basicConfig(
    filename=os.path.join("log", f'{os.path.basename(__file__).split(".py")[0]}_{dt.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")}.log'),
    format="%(levelname)s | %(asctime)s | %(message)s",
    datefmt="%m/%d/%Y-%I:%M:%S",
    level=logging.INFO,
)