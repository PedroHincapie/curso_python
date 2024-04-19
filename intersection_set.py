# intersecption() keep ONLY the duplicate
# will return a new set, that only contains the items that are present in both sets
# you can use & operator instead of the intersecption() method

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set_3 = set1.intersection(set2)
print(set_3)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set_4 = set1  & set2
print(set_4)

'''
Note: The & operator only allows you to join sets with sets, 
and not with other data types like you can with the intersecton() method.
'''

# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)

#The difference() method will return a new set that will contain only the items
# from the first set that are not present in the other set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)

# Note: The - operator only allows you to join sets with sets, 
# and not with other data types like you can with the difference() method.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)

'''
The difference_update() method will also keep the items from the first set that are not in the other set, 
but it will change the original set instead of returning a new set.
'''
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)


countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

new_set = set(countries | northAm | centralAm | southAm)

print(new_set)
# Escribe tu solución 👇


