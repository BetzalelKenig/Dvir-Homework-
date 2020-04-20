import numpy as np
​
def remove_duplicate(l):
    return set(l)
​
​
print(remove_duplicate(['Moshe', 'Ahron', 'Shlomo', 'Ahron']))
​
​
def remove_duplicate2(l):
    new_list = []
    for w in l:
        if w not in new_list:
            new_list.append(w)
    return new_list
​
​
print(remove_duplicate2(['Moshe', 'Ahron', 'Shlomo', 'Ahron']))
​
​
def lesson_subject(cours, week_num, lesson_num):
    courses = {'python': [['python one', 'python tow'], ['python tree', 'python for']],
               'math': [['math one', 'math tow'], ['math tree', 'math for']],
               'devops': [['devops one', 'devops tow'], ['devops tree', 'devops for']]}
    try:
        return courses.get(cours.lower())[week_num - 1][lesson_num - 1]
    except IndexError:
        print('Invalid input')
    except TypeError:
        print('Invalid input')
​
​
#print(lesson_subject('math', 2, 1))
​
def matrix(num):
    for i in range(num):
        for j in range(num):
            print('0' if i ^ j else '1', end=',')
        print()
​
​
#print(matrix(5))
​
def matrix_xo(num):
    for i in range(num):
        for j in range(num):
            print('o' if i != j else 'x', end=',')
        print()
​
​
#print(matrix_xo(5))
​
for i in range(3):
    for j in range(5):
        if (i == j) or (i + j == 4):
            print(end="x")
        else:
            print("o", end="")
    print('')
​
def matrix_mult(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(i * j, end='\t')
        print()
​
​
#matrix_mult(10)
​
try_sum_result = {'ending': [0, 0], 'sum': [0, 0]}
​
​
def try_sum(target=200, undivided=3, step=2):
    counter = 0
    sum = 0
    for n in range(2, target, step):
        if n % undivided != 0 and counter % 2 == 0:
            sum += n
            print(n, end=' ')
        if n % undivided != 0:
            counter += 1
        if sum > target:
            try_sum_result['ending'][1] += 1
            try_sum_result['ending'][0] += n
            try_sum_result['sum'][1] += 1
            try_sum_result['sum'][0] += sum
            print(f'\nSum of multiples of {step} undivided by {undivided} from 0 to {n} = {sum}')
            break
​
​
print(try_sum(target=200))
print(try_sum(target=300))
print(try_sum(undivided=7))
print(try_sum(step=3, undivided=2))
​
ans = input('Which average would you like to print? (ending/sum)\n')
if ans in try_sum_result:
    print(try_sum_result[ans][0] / try_sum_result[ans][1])
else:
    print('No such parameter')