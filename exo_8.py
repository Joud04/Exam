#Écrivez un programme Python qui itère les entiers de 1 à 50. Pour les multiples de trois,
#imprimez « Fizz » au lieu du nombre et pour les multiples de cinq, imprimez « Buzz ». Pour les nombres multiples de trois et cinq, imprimez « FizzBuzz ».

# On va de 1 à 50 (donc range doit aller jusqu'à 51)
for nombre in range(1, 51):
    if nombre % 3 == 0 and nombre % 5 == 0:
        print("FizzBuzz")
        
    elif nombre % 3 == 0:
        print("Fizz")

    elif nombre % 5 == 0:
        print("Buzz")
        
    else:
        print(nombre)
