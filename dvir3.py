r,l = range(10),'\n'
print('#x:',['#'+str(x) for x in r],l,'x/2:',[x/2 for x in r],l,'x**2:',[x**2 for x in r])
​
​
d = {m: [eval(m) for x in range(10)] for m in ['x*5','x/2','x**2','x%3','x+3','x-1']}
for i in d: print(i+':',d[i])
​
def operation(a):
    return lambda b: a * b
​
double = operation(2)
triple = operation(3)
print(double(5))
print(triple(5))
​
​
from functools import reduce
​
def revers_str(str):
    return str[::-1]
​
print(revers_str('goal'))