### Function in Python

- ##### Creating a Function

```
def my_first_funtion():
    print("Hello Mon")    

def my_first_funtion_with_arguments(name):
    print(f"Hello {name}")
```

- ##### Calling a Functios

```
my_first_funtion()
my_first_funtion_with_arguments('Pedrito')
```

- ##### Number of Arguments
By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.

- ##### Arbitrary Arguments, *args
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:
```
def sum_age(*ages):
    print(ages)
    print(type(ages))
    sum = int(0)
    for age in ages:
        sum += age
        print(sum)
    return sum

restul = sum_age(2,6)
print(f"La edad total de los alumnos es {restul}")
```

- ##### Default Parameter Value
The following example shows how to use a default parameter value.

If we call the function without argument, it uses the default value:

```
def my_city(city="Medellin"):
    print(city)

my_city('Bogota')
my_city()
```

### Zen Python
```
import this
```
Esta es la filosofia con la que cronstruye y construyo Python

### Set Python

Este es otro tipo de dato en Python, tenemos ahora a los conjuntos, que son un tipo de datos que nos permite:

- No tienen un orden
- No permite duplicaco como los diccionarios
- Puedes modificar

Cuando se dice que no tiene un orden, es por que cada vez que se ejecuta el print de este tipo de clases set, el valor itera por cada, asi las cosas no existe un orden dentro de este

```
set_paises = {
    'Colombia', 'Mexico', 'Argentina'
}

print(set_paises)

```
Ademas cabe mencionar que en un set un 1 es igual a True por lo que si los dos estan en un set solo quedara True y esto aplica para el False y el 0 pero en esta ocacion no queda el False, queda el 0

- Len para los set
```
# Ejercicio del False == 0
thisset = {0, "banana", "cherry", False,  2}

print(thisset)

print(len(thisset))

```



### Lambda in Python

A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.