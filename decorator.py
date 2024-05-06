def my_decorator(func):
    def wrapper():
        print('hello world')
        func()
        print('hi')
    return wrapper


@my_decorator
def hello():
    print('hello my name')


hello()
