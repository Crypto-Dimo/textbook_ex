# person

jako = {
    'name': 'giacomo',
    'surname': 'chiovo',
    'age': 29,
    'city': 'selinunte',
    }

name = jako['name'].title()
surname = jako['surname'].title()
age = jako['age']
city = jako['city'].title()

print(f"Name: {name}\nSurname: {surname}\nAge: {age}\nCity: {city}")
print("\n")
# favourite number

favourite_numbers = {
    'jako': 14,
    'iris': 12,
    'ezra': 16,
    'ada': 11,
    'franci': 17,
    }

jako_number = favourite_numbers['jako']
iris_number = favourite_numbers['iris']
ezra_number = favourite_numbers['ezra']
ada_number = favourite_numbers['ada']
franci_number = favourite_numbers['franci']

print(f"Jako's favourite number is {jako_number}.\nIris's favourite number is {iris_number}.\nEzra's favourite number is {ezra_number}.\nAda's favourite number is {ada_number}.\nFranci's favourite number is {franci_number}.")
print("\n")

# glossary

glossary = {
    'dictionary': 'list of objects with a key and a value',
    'tuple': 'list of objects that cannot be changed',
    'turtle': 'module mainly used to teach kids programming',
    'variable': 'object with a specified value',
    'integer': 'obect representing a whole number',
    }

print(f"A dictionary is a {glossary['dictionary']}.\nA tuple is a {glossary['tuple']}.\nA turtle is a {glossary['turtle']}.\nA variable is a {glossary['variable']}.\nAn integer is an {glossary['integer']}.")
