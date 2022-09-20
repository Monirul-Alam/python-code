from  utility import  divide, multiply
from  shopping.more_shopping_cart import shopping_cart
import  random
# print(shopping_cart.buy('apple'))
# print(divide(4,2))
# print(multiply(2,3))
# print(__name__)
print(random)
print(random.random)# it tells you random is a function
print(random.random())## it will choose 0 and 1
print(random.randint(1,10))## it will choose 1 to 10
print(random.choice([1,2,3,4,5,6]))# it will choose from the list

my_list =[1,2,3,4,6,7,8]
random.shuffle(my_list)#it will shuffle
print(my_list)