from collections import  defaultdict,Counter,OrderedDict
import  datetime
from array import  array

list =[1,2,4,5,6,21,4,3,52,5,21,1]

sentence = 'bla blah lol how did you done that this silly mistake!'

# print(Counter(list))
# print(Counter(sentence))

# dictionary =defaultdict(lambda : 'doesnt exits',{'a':1,
#              'b':2})
# print(dictionary['c'])

d = OrderedDict()
d['a']=1
d['b']=2

d2 =OrderedDict()
d2['a']=1
d2['b']=2
#print(d == d2)
# print(datetime.time(5,23,2))
# print(datetime.date.today())


arr = array('I',[1,2,3])
print(arr[1])
