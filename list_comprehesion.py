# List comprehesion
list_number = []

# Estas es la forma tradicional en donde tenemos varias lienas de codigo y una sintaxis mas compleja
print("*** " * 10)
for item in range(1, 10):
    list_number.append(item)
print(list_number)

# aqui aplicamos list comprehesion vemos que en una sola linea tenemos el mismos resultado
list_number.clear()
list_number = [item for item in range(1, 10)]
print(list_number)

print("*** " * 10)
# Si ahora al elemento que obtengo, le deseo realizar una operacion
list_number.clear()
for item in range(1, 10):
    list_number.append(item * 2)
print(list_number)

# En un list comprehesion
list_number.clear()
list_number = [item *2 for item in range(1, 10)]
print(list_number)

print("*** " * 10)
# Si ahora al elemento que obtengo, le deseo realizar una condicion
list_number.clear()
for item in range(1, 10):
    if item % 2 == 0:
        list_number.append(item)
print(list_number)

list_number = [item for item in range(1, 10) if item % 2 == 0 ]
print(list_number)
