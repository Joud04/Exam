#Écrivez un programme Python pour trouver les nombres divisibles par 7 et multiples de 5, entre 1 500 et 2 700 (tous deux inclus).

resultats = []

for nombre in range (1500, 2701): 
    if (nombre % 7 == 0) and (nombre % 5 == 0):
        print(nombre)