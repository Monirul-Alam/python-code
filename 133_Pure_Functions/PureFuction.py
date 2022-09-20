# Pure functions
# def multiply_by_2(li):
#     new_list = []
#     for item in li:
#         new_list.append(2 * item)
#     return new_list
#
#
# print(multiply_by_2([1, 2, 3]))


# map()
# new_list =[1,2,3]
# def multiply_by_2(item):
#
#     return item * 2
#
#
# print(list(map(multiply_by_2,new_list)))
# print(new_list)

# filter()

# new_list =[1,2,3]
# def multiply_by_2(item):
#
#     return item * 2
# def only_odd(item):
#     return  item %2!=0
#
# print(list(filter(only_odd,new_list)))
# print(new_list)

# zip()

# new_list =[1,2]
# your_list ={
#     'a' : 1,
#     'b' : 2
# }
# def multiply_by_2(item):
#
#     return item * 2
# def only_odd(item):
#     return  item %2!=0
#
# print(list(zip(new_list,your_list)))
# print(new_list)
# print(your_list)



# reduce()
# from functools import  reduce
# new_list =[1,2,3]
#
# def only_odd(item):
#     return  item %2!=0
# def accumulator(acc,item):
#     print(acc, item)
#     return acc + item
#
# print(reduce(accumulator,new_list, 0))
# print(new_list)


# my_list =[5,4,3]
#
# new_list = list(map(lambda item :item** 2 ,my_list))
# print(new_list)
a= [(2,4),(4,-1),(10,8),(3,3)]

a.sort(key= lambda item : item[1])
print(a)
a.reverse()
print(a)