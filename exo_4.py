#Écrivez un programme Python qui accepte une chaîne et calcule le nombre de chiffres et de lettres

string = input("Saisir une phrase: ")

chiffres = 0
lettres = 0

for char in string:
    if char.isdigit():
        chiffres += 1
    
    elif char.isalpha():
        lettres += 1

print("Nombres de chiffres: ", chiffres)
print("Nombre de lettres: ", lettres)
