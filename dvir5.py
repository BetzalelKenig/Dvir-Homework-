from matplotlib._color_data import TABLEAU_COLORS, CSS4_COLORS, XKCD_COLORS
import datetime
import logging
​
time_st = '{0:%Y_%m_%d_%H_%M}'.format(datetime.datetime.now())
​
​
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
​
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
​
file_handler = logging.FileHandler('color.log')
file_handler.setFormatter(formatter)
​
logger.addHandler(file_handler)
​
nbc_logger = logging.getLogger(f'nonBaseColorLog')
logger.setLevel(10)
file_handler2 = logging.FileHandler(f'nbc{time_st}.log')
file_handler2.setFormatter(formatter)
nbc_logger.addHandler(file_handler2)
​
​
​
class ColorError(Exception):
    pass
​
​
class NonColor(ColorError):
    def __init__(self, m):
        logger.warning(f'{m} is not a colour')
​
​
class NonBaseColor(Exception):
​
    def __init__(self):
        print('''Only base colours allowed
    Try  again''')
​
​
​
primary_color = ['red', 'green', 'blue']
​
​
def ask_color():
    while True:
        user = input('Choose base color: ')
        check_user = user.strip().lower()
        try:
            if check_user in primary_color:
                print(user)
                continue
            if check_user in XKCD_COLORS or user in CSS4_COLORS or user in TABLEAU_COLORS:
                nbc_logger.warning(f'{user} is nut base color')
                raise NonBaseColor
            else:
                raise NonColor(user)
        except NonBaseColor as nbc:
            nbc_logger.warning(nbc)
        finally:
            logger.debug(f'printing colour request handled for {user}')
​
​
ask_color()