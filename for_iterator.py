fruits = list(('apple', 'banana', 'cherry'))
print(fruits)

for value in fruits:
    if value == 'banana':
        continue
        #break con este no llega al final, solo sale del ciclo
    print(value)
else:
    print('Finally finished!')

print('-'*10)
for x in []:
    pass

for value in range(len(fruits)):
    print(value, fruits[value])
    
print('-'*10)
    
[print(value) for value in fruits]
    