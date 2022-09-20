# def hello(func):
#     func()
#
# def greet():
#     print('Still here!')
# a =hello(greet)

# print(a)

# def my_Decorator(func):
#     def wrap_func():
#       print("*******")
#       func()
#       print("******")
#     return wrap_func

# @my_Decorator
# def hello():
#     print("Helloooo!")
# hello()
# ///////////////////////
# my_Decorator() procedure!
# hello2 =my_Decorator(hello)
# hello2()
# ////////////////////
# decorator pattern
def my_Decorator(func):
    def wrap_func(*args,**kwargs):
      print("*******")
      func(*args, **kwargs)
      print("******")
    return wrap_func
@my_Decorator
def hello(greeting , emoji):
    print(greeting, emoji)

hello('hii',':))')