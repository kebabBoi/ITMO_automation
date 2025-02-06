class Mammal:
    className = 'Млекопитающее'

class Dog(Mammal):
    species = 'Canis lupus'

dog = Dog()
print('Это животное ' + dog.className + ' так еще и вида ' + dog.species)