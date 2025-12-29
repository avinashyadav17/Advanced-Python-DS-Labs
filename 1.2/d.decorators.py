def my_decorator(func):
    def wrapper():
        print("before function")
        func()
        print("after function")
    return wrapper

def say_hello():
    print("hello")

say_hello=my_decorator(say_hello)
say_hello()
