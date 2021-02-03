# example 1

age = 12

if age < 4:
    print('Your admission cost is $0.')
elif age < 18:
    print('Your admission cost is $25.')
else:
    print('Your admission cost is $40.')

# example 2 (shorter version and better)
# in this case the else is for older than age 65 who have 50% discount 
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f'Your admission cost is ${price}.')

# not always you need to end with an 'else' like below

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f'Your admission cost is ${price}.')