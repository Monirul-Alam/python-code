def generator_code(item):
    for i in range(item):

     yield i*2

g= generator_code(100)
next(g)
next(g)

print(next(g))
print(next(g))