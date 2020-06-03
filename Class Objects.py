# Defining a first class object 

def greeting(language):
    if language == 'eng':
        return 'hello world'
    elif language == 'fr':
        return 'Bonjour le monde'
    else: 
        return 'language not supported' 

l=[greeting('eng'), greeting('fr'), greeting('ger')]
print(l[1])

# Calling functions from previous defined functions

def callf(f):
    lang = 'eng'
    return (f(lang))

print(callf(greeting))

