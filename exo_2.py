#Écrivez un programme Python pour trouver la médiane parmi trois nombres donnés comme input

def trouver_mediane(a,b,c):

    liste_nombres = [a,b,c]

    liste_nombres.sort()

    return liste_nombres[1]

x = float(input("Entrez un 1er nombre: "))
y = float(input("Entrez un 2ème nombre: "))
z = float(input("Entrez un 3ème nombre: "))

resultat = trouver_mediane(x,y,z)
print("La médiane de ces nombres est: ", resultat)

"""Input the first number 25
Input the second number 15
Input the third number 35
Median of the above three numbers 
25"""