# Écrivez une fonction Python qui prend une séquence de nombres et détermine si tous les nombres sont différents les uns des autres.

def test_distinct(data) :
    deja_vus = []

    for nombre in data :
        if nombre in deja_vus:
            return False
        
        deja_vus.append(nombre)

    return True

print(test_distinct([1, 5, 7, 9]))
print(test_distinct([2, 4, 5, 5, 7, 9]))
