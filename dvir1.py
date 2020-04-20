import math
inp = ['h', 'e', 'l', 'o', 'p', 'y', 't', 'h', 'o', 'n', 7.6]
num = str(inp[-1])
n = str(int(num[2]) // 2) + str(num[1]) + str(math.ceil(float(inp[-1])))
hello_python = inp[0].upper() + ''.join(inp[1:3]) + inp[2] + inp[3] + ' ' + ''.join(inp[4:-1]) + ' ' + n
print(hello_python)
​
​
def nis_to_usd():
    try:
        nis = input("Enter number of Shekel:\n")
        print(str(int(nis) * 3) + '$')
    except ValueError:
        print("Only numbers")
​
​
#nis_to_usd()
​
​
def syco():
    inp = input('What?\n')
    while inp:
        try:
            inp = input(inp.split(' ', 1)[1] + '?\n')
        except IndexError:
            inp = input('At least tow word:\n')
            continue
​
​
#syco()
​
​
def replace_to_e():
    user_input = input('Enter a string:\n')
    before, first, after = user_input.partition(user_input[0])
    result = before + first + after.replace(user_input[0], 'e')
    print(result)
​
​
#replace_to_e()