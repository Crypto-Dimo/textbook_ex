favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

language = favourite_languages['sarah'].title()

print(f"Sarah's favourite language is {language}.")

# using loop and .items() method

for name, language in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}.")

# using loop and .keys() method

for name in favourite_languages.keys():
    print(name.title())

# using loop without .keys() == as using .keys()

for name in favourite_languages:
    print(name.title())

# how to select some keys to print 

friends = ['phil', 'sarah']

for name in favourite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favourite_languages[name].title()
        print(f"\t{name.title()} I see you love {language}!")


if 'erin' not in favourite_languages.keys():
    print(f"Erin, please take our poll!")

# looping in a particular order with sorted() mothod

for name in sorted(favourite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# using loop for values

print("\nThe following languages have been mentioned:\n")

for language in favourite_languages.values():
    print(language.title())

print("\n")

# using set() to avoid repetitions

for language in set(favourite_languages.values()):
    print(language.title())

# example of a set
# languages = {'python', 'ruby', 'c'}

# nesting

favourite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favourite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favourite languages are:")
        for language in languages:
            print(f"\t- {language.title()};")
    else:
        print(f"\n{name.title()}'s favourite language is {language.title()}.")