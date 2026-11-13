print('')


llista =[]
llista.append(input("Introdueix un nom: "))      
llista.append(input("Introdueix un nom: "))      
llista.append(input("Introdueix un nom: "))      


#amb bucle

for i in range(3):
    llista.append(input("Introdueix un nom: "))

print('')
print(llista)
print('')

for i in range(17,101):
    if i % 2 == 0:
        print(i, end=' ')
print("\n")

notes = [[6,6,7,10,9],[10,7,6,7,7],[5,5,10,7,10]]
n= 0
posicion=[]
for i in notes:
    for i in i:
        if i == 10:
            n+= 1
            posicion.append((notes.index(i), i.index(i)))
