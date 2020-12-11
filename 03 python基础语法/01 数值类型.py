"""
文件说明

"""
# a = 10.2
# print(type(a))
s = 'this is a book'
print(list(s))
#  ['t', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 'b', 'o', 'o', 'k']
s2 = s.split()
print(list(s2))
# ['this', 'is', 'a', 'book']

alist = ['this', 'is', 'a', 'book']
strA = ' '.join(alist)
print(strA)
#  this is a book
