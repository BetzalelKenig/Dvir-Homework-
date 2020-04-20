from matplotlib._color_data import TABLEAU_COLORS, CSS4_COLORS, XKCD_COLORS
​
​
class ColorError(Exception):
    pass
​
​
class NonColor(ColorError):
    def __init__(self, m):
        print(f'{m} is not a colour')
​
​
class NonBaseColor(Exception):
​
    def __init__(self):
        print('''Only base colours allowed
    Try  again''')
​
​
primary_color = ['red', 'green', 'blue']
​
​
while True:
    user = input('Choose base color: ')
    check_user = user.strip().lower()
    try:
        if check_user in primary_color:
            print(user)
            continue
        if check_user in XKCD_COLORS or user in CSS4_COLORS or user in TABLEAU_COLORS:
            raise NonBaseColor
        else:
            raise NonColor(user)
    except NonBaseColor as nbc:
        print(nbc)
    finally:
        print('printing colour request handled...')