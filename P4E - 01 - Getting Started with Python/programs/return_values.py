#def greet():
#    return "Hello"

#print(greet(), "Glenn")
#print(greet(), "Sally")


def greet(lang):
    if lang == 'es':
        return "Hola"
    elif lang == 'fr':
        return "Bonjour"
    else: 
        return "Hello"

print(greet('en'), 'Gleen')
print(greet('es'), 'Sally')
print(greet('fr'), 'Michael')