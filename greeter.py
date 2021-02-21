def greet_user():
    """Display a simple greeting."""
    print('Hello!')


greet_user()


# adding a value to the function

def greet_user(username):
    """Display a simple greeting."""
    print(f'Hello, {username.title()}!')

# adding a loop


names = ['jako', 'franci', 'ele']

for name in names:
    greet_user(name)
