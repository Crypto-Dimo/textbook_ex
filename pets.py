trixie = {
    'kind': 'chihuahua',
    'owner': 'matt',
    }

francine = {
    'kind': 'doberman',
    'owner': 'roger',
    }

stan = {
    'kind': 'dalmatian',
    'owner': 'steve',
    }

ada = {
    'kind': 'beagle',
    'owner': 'marco',
    }

tiago = {
    'kind': 'cocker',
    'owner': 'cristian',
    }

pets = [trixie, francine, stan, ada, tiago]

for pet in pets:
    print(f"\nKind: {pet['kind'].title()}\nOwner: {pet['owner'].title()}")