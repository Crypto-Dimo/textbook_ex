age = int(input('Enter your age: '))

if age < 3:
    ticket = 0
elif 3 < age < 12:
    ticket = 12
else:
    ticket = 15

print(f'The ticket price is ${ticket}')