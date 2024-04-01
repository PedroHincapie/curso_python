# Set pueden ser de cualquier tipo
set_paises = {"Colombia", "Mexico", "Argentina"}
print(set_paises)

set_type = {
    True,
    "Col",
    123,
    8.7,
}
print(set_type)

# construcutor de la clase set
this_is_set = set(("23", 4))
print(this_is_set)

# Puedes hacer la conversion de cualquier tipo
# iterable a set, list , tupla, dict
set_string = set("Hola")
print(set_string)

this_is_list = list(["D", 4])
print(this_is_list)


this_is_list = tuple(("D", 4))
print(this_is_list)

this_is_list = dict(name=2)
print(this_is_list)

# Ejercicio del True == 1
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# Ejercicio del False == 0
thisset = {0, "banana", "cherry", False, 2}
print(thisset)

# Conocer el tamaño
print(len(thisset))

# Tipo
print(type(thisset))


# Operaciones con conjuntos
this_is_set_countries = {"Col", "Pe", "Argentina"}
print(this_is_set_countries)

# Adicionar elementos a un conjunto
this_is_set_countries.add("Chile")
print(this_is_set_countries)


# Adicionar elementos a un conjunto
this_is_set_countries.add("Chile")
print(this_is_set_countries)
