favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

people = ['jen', 'sarah', 'edward', 'phil', 'ewan','iris']

for name in people:
    if name in favourite_languages:
        print(f"Thank you for taking the poll {name.title()}.")
    else:
        print(f"{name.title()}, please take the poll.")

