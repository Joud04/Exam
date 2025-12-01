def longueur(s):
    mots = s.split()
    if len(mots) == 0:
        return 0
    dernier_mot = mots[-1]
    return len(dernier_mot)

print(longueur("Hello World"))                
print(longueur(" Envole-moi vers la lune "))   
print(longueur("Luffy est toujours Joyboy"))  