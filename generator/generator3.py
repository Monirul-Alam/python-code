def special_generator(iterable):
    iterator = iter(iterable)

    while True:
       try:
        print(iterator)
        print(next(iterator)*2)
       except StopIteration:
           break
special_generator([1,3,5])
print("_____________________________")

# range???????
class mygen:
    current = 0
    def __init__(self, first,last):
        self.first = first
        self.last = last
    def __iter__(self):
        return  self
    def __next__(self):
        if self.first<self.last:
           num = self.first
           self.first+=1
           return  num
        raise  StopIteration



gen = mygen(5,10)

for i in gen:
    print(i)
