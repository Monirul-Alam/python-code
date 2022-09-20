import re
#
# pattern =re.compile("this ")
#
# string = ("this is it this two ")
#
# a = pattern.search(string)
# b=pattern.findall(string)
# c =pattern.fullmatch(string)
# d = pattern.match(string)
# print(a.group())
# print(b)
# print(c)
# print(d)
password ="snisdjdndj11?8"
pattern2 =re.compile(r"[A-Za-z0-9#%?]{8,}\d")
checker = pattern2.fullmatch(password)

print(checker)