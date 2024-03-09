text = "Hola me encanta Python"

# para analizar si detro de una cadena de string existe una palabra 
print("Python" in text)

print("Js" in text)

# Para conocer el tamañno de un string
print(len(text))

#Transformar minusculas mayusculas
print(text.upper())


print(text.lower())

print(text.capitalize())

# Cuando nocesita saber cual es la cantidad de letras en un texto
print(text.count("a"))
#Ten presente lo que son las sencibilidad de las letras
print(text.count("p"))
print(text.count("P"))

#swapcase en el inverso al capitalizer
print(text)
print(text.swapcase())

#Para conocer si un texto inicia por una palabra especifica tenemos
print(text.startswith("Holi"))


#Para conocer si un texto finaliza por una palabra especifica tenemos
print(text.endswith("Holi"))

#Para remplazar
print(text.replace("Hola", "Holi"))

#Para aplicar capítalizer a todos las palabras de una frase tensmos
print(text.title())

#Para conocer si un texto es un digito
print(text.isnumeric())
print(text.isdigit())



