import inspect
functions = []
def register(func):
    def wrapper_function(*args, **kwargs):
        print(f'register function {func.__name__}')
        functions.append(f'{func.__name__}{args,kwargs}')
        return func(*args, **kwargs)
    return wrapper_function


def unregistered(masg):
    return masg


@register
def printer(greet):
    print(greet)

@register
def duplicator(*args):
    return [[i, i] for i in args]


@register
def kwfunc(x=5, y=300):
    print(x*y)

printer('hi')
print(duplicator(5, 6, '7'))
print(duplicator('r'))
print(unregistered('i\'m under the radar'))
kwfunc()
kwfunc(x=5, y=3)
print('The calls to registered functions in this system are:')
[print(f) for f in functions]