print("")

print("Benvingut al joc d'endevinar la combinació de 4 números!")

llista = ["1", "2", "3", "4", "5", "6"]
import random
secret = random.sample(llista, 4)
comptador = 0
print(secret)
while (comptador < 10):
    comptador += 1
    print("")
    print("Introdueix una combinació de 4 números entre 1 i 6, separats per espais:")
    combinacio = input().split()
    print(combinacio)
    
    encerts = sum(1 for i in range(4) if combinacio[i] == secret[i])
    coincidencies = sum(min(combinacio.count(num), secret.count(num)) for num in set(combinacio))

    print(f"Encerts: {encerts}, Coincidències: {coincidencies}")

    if encerts == 4:
        print("Felicitats! Has endevinat la combinació secreta!")
        break

