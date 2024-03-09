my_list = ['Pedro', 'Hector', 'Marlon', 3]
print(my_list)

# Revertir el orden de una lista
my_list.reverse()
print(my_list)

my_list.append(34345)
print(my_list)

my_list.clear()
print(my_list)


my_list.append(34345)
copi = my_list.copy()
copi.append(23)
copi.append(3)
copi.append(3)

print(my_list)
print(copi)

my_list.extend(copi)
print(my_list)

my_list.insert(2,True)
print(my_list)

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
thislist.sort()
print(thislist)

print("***" * 20 )



def my_funct(e):
    return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

print(cars)

print(">>>")

cars.sort(key=my_funct)
print(cars)

print(">>>")

cars.sort(reverse=True,key=my_funct)

print(cars)