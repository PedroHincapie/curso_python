'''
There are several way to join two or more sets in Python
'''

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

'''
Union and Update methods joind all items from both sets
'''

'''
union() method returns a new set will all items from both set
| operator instead of the union() method, and you will get the same result
but only allows join set with sets, and not with other type like you can with the union()
'''
myset = set1.union(set2, set3, set4)
print(myset)

myset = set1 | set2 | set3| set4
print(myset)

set_3 = set1.union(set2)
print(set_3)

set_4 = set1 | set2
print(set_4)

# union() any type like
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

# | operator can not any type like
x = {"a", "b", "c"}
y = (1, 2, 3)

'''
z = x | y
print(z)
TypeError: unsupported operand type(s) for |: 'set' and 'tuple'
'''

'''
The update() method inserts all items from one set into another.
The update() changes the original set, and does not return a new set.
'''
set1.update(set_3)
print(set1)
