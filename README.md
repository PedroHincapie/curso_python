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


### Lambda in Python

A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.