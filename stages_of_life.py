age = 2

if age < 2:
    print("It's a baby.")
elif age >= 2 and age < 4:
    print("It's a toddler.")
elif age >= 4 and age < 13:
    print("It's a kid.")
elif age >= 13 and age < 20:
    print("It's a teenager.")
elif age >= 20 and age < 65:
    print("It's an adult.")
else:
    print("It's an elder.")

# example with input

age = int(input("what's the person's age?"))

if age < 2:
    print("It's a baby.")
elif age >= 2 and age < 4:
    print("It's a toddler.")
elif age >= 4 and age < 13:
    print("It's a kid.")
elif age >= 13 and age < 20:
    print("It's a teenager.")
elif age >= 20 and age < 65:
    print("It's an adult.")
else:
    print("It's an elder.")