#Écrire un programme Python pour compter le nombre de nombres pairs et impairs dans une série de nombres

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

pair = 0
impair = 0

for nombre in numbers:
    if nombre % 2 == 0:
        pair += 1
    else:
        impair += 1

print("Nombre de nombres pairs :", pair)
print("Nombre de nombres impairs :", impair)


