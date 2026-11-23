print("")

print("Benvingut al joc d'endevinar la combinació de 4 números!")
print("Escull una dificultat:")
print("(1) Fàcil (10 intents)")
print("(2) Mitjà (7 intents)")
print("(3) Difícil (5 intents)")
print("Introdueix el número corresponent a la dificultat desitjada:")
dificultat=input()
if dificultat == "1":
    intents = 10
elif dificultat == "2":
    intents = 7
elif dificultat == "3":
    intents = 5
else:
    print("Dificultat no vàlida.Es seleccionara la dificultat fàcil.")
    intents = 10

llista = ["1", "2", "3", "4", "5", "6"]
import random
secret = random.sample(llista, 4)
comptador = 0

while (comptador < intents):
    comptador += 1
    print("")
    print("Introdueix una combinació de 4 números entre 1 i 6, separats per espais:")
    combinacio = input().split()
    #split serveix per posar el text entre espais i separar-lo en una llista
    print(combinacio)
    if any(num not in llista for num in combinacio) or len(combinacio) != 4:
        print("Combinació invàlida. Assegura't d'introduir 4 números entre 1 i 6.")
        comptador -= 1  # No comptar aquesta ronda com a intent vàlid
        continue

    encerts = sum(1 for i in range(4) if combinacio[i] == secret[i])
    coincidencies = sum(min(combinacio.count(num), secret.count(num)) for num in set(combinacio))

    print(f"Encerts: {encerts}, Coincidències: {coincidencies}")
    #f serveix per introduir variables dins d'un print amb {} i que es mostrin correctament

    if encerts == 4:
        print("Felicitats! Has endevinat la combinació secreta!")
        break
else:
        print(f"No has endevinat la combinació secreta, la combinació era: {secret}")
        
   

#el break es el que fa que s'aturi el while

