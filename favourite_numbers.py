favourite_numbers = {
    'jako': [14, 19],
    'iris': [12, 20],
    'ezra': [16, 21],
    'ada': [11, 34],
    'franci': [17, 56],
    }

for name, numbers in favourite_numbers.items():
    print(f"{name.title()}' favourite numbers are:")
    for number in numbers:
        print(f"\t- {number}")