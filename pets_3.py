# functions and positional arguments - always maintain the same order

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f'\nI have a {animal_type}.')
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('dog', 'ada')
describe_pet('hamster', 'harry')

# keyword arguments - no need for specific order


def describe_pet_2(animal_type_2, pet_name_2):
    """Display information about a pet."""
    print(f'\nI have a {animal_type_2}.')
    print(f"My {animal_type_2}'s name is {pet_name_2.title()}.")


describe_pet_2(animal_type_2='hamster', pet_name_2='harry')

# the two are equivalent

describe_pet_2(pet_name_2='harry', animal_type_2='hamster')

# default values


def describe_pet_3(pet_name_3, animal_type_3='dog'):
    """Display information about a pet."""
    print(f'\nI have a {animal_type_3}.')
    print(f"My {animal_type_3}'s name is {pet_name_3.title()}.")


describe_pet_3('ada')

# if you want to change the animal do as follows

describe_pet_3(pet_name_3='harry', animal_type_3='hamster')
