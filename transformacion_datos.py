#Python es un lenguaje que infiere apartir de su contenido
variable = "Pedro Hincapie"
print(variable)


variable = 'Hincapie'
print(variable)

variable = False
print(variable)

variable =not False
print(variable)

variable = 2323
print(variable)


variable = 3.4444
print(variable)

#print("My edad es" + age) Esto falla, por que al inferinir
#NO es capaz de hacer la operacion
#age = 34
#print("My edad es" + age)

age = 34
print("My edad es", age)

age = 34
template = f"My edad es {age}"
print(template)

template = "My edad es {}".format(age)
print(template)


print("Mi edad es " + str(age+1))

edad  = input("Cual es tu edad : ")
print(edad)

#Ahora calculamos la edad en 20 años
#print("Tu edad en 20 años sera de ", edad+20)
#Esto falla, y es por que no puede hacer operaciones con str

#Por lo que aplicamos la conversion de str to int
edad = int(edad)
edad +=20
print("Tu edad en 20 años sera de ", edad)






