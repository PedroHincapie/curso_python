def my_first_funtion():
    print("Hello Mon")


def my_first_funtion_with_arguments(name):
    print(f"Hello {name}")


my_first_funtion()
my_first_funtion_with_arguments("Pedrito")


def sum_age(*ages):
    print(ages)
    print(type(ages))
    sum = int(0)
    for age in ages:
        sum += age
        print(sum)
    return sum


restul = sum_age(2, 6)
print(f"La edad total de los alumnos es {restul}")


def my_city(city="Medellin"):
    print(city)

my_city('Bogota')
my_city()
