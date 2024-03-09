name = "jaimito Angulo"
last_name = 'Martin'

# la concatenacion es +
print(name + last_name)

#Operaciones autoincrentar

edad = 12
edad += 2
print(edad)
print(type(edad))

full_name = name + last_name

print(full_name)

# Algunas consideraciones si el texto tienen comillas simple o dobles, 
#encapsula la sentencia en la inversa

#last_name = 'I' ma'
#greeting = " She said "Hello" "

# format in string
#Forma de darle uns estrutura a un mensajes

template_name = "V1 Hola mi nombre es " + name + " y mi apellido es " + last_name
print(template_name)

template_2 = "V2 Hola mi nombre es {} y mi apellido es {}".format(name, last_name)
print(template_2)

template_3 = f" V3 Hola este es mi nombre {name} y mi apellido es {last_name}"
print(template_3)