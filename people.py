# people

jako = {
    'name': 'giacomo',
    'surname': 'chiovo',
    'age': 29,
    'country': 'italy',
    }

marco = {
    'name': 'marco',
    'surname': 'di maio',
    'age': 30,
    'country': 'uk',
    }

frank = {
    'name': 'frank',
    'surname': 'smith',
    'age': 27,
    'country': 'usa',
}

people = [jako, marco, frank]


for person in people:
    print(f"\nName: {person['name'].title()}\nSurname: {person['surname'].title()}\nAge: {person['age']}\nCountry: {person['country'].title()}")
