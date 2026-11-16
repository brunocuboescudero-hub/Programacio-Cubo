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
fila = 0
for lista in notes:
    columna = 0
    for nota in lista:
        if nota == 10:
            posicion.append([fila,columna])
            n += 1
        columna += 1
    fila += 1
print ("El número 10 sale: ", n)
print("posiciones: ", posicion)
