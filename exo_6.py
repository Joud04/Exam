#Écrivez un programme Python pour convertir les températures vers et depuis Celsius et Fahrenheit.

temperature = input("Saisir la température (102F, 30C): ")
unite = temperature[-1].upper()
nombre = int (temperature[:-1])

if unite == "C" :
    resultat = (nombre * 9/5) + 32
    print(nombre, " est égal à ", int(resultat), "F")

elif unite == "F" :
    resultat = (nombre - 32) * 5/9
    print(nombre, " est égal à ", int(resultat), "C")

else:
    print("Bien saisir la température au format 30C")