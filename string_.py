text = "Python es un excelente lenguaje"
"""
De esta forma puedes reconcer si tendro de un strign existe
o no el contenido
"""
# aqui estamos haciendo uso many values to multiple variable
result, r = "Java" in text, "Python" in text
print(result, r)

# Recuerdas que un string are arrays
text = """ Hola Mariana, las cosas no salieron como lo pensamos,
Hay que terminrar
"""
print(text)

# This is a example
print(text[1])

text = 'Nunca pares de pensar en el Futuro'

# I can looping to string
for value in text:
    print(value)  

print('----'*10)
# I can know length string
print(len(text))

if 'w' not in text:
    print('Lo siento, no esta presente', 'w')

print('----'*10)
# Recuerda que como los string son Arrays tu
#Puedes realizar slicing

text_nunca = text[:5]
print(text_nunca)
text_nunca = text[0:5]
print(text_nunca)



text_final = text[15:] #pensar en el futuro
print(text_final)


text = "ama mi ma"
este_es_igual_al_text = text[::]
invertir_text = text[::-1]

print('text =>', text)
print('este_es_igual_al_text =>', este_es_igual_al_text)
print('invertido =>', invertir_text)
