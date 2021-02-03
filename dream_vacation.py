responses = {}

poll_active = True

while poll_active:
    name = input('What is your name? ')
    response = input('If you could visit a place in the world, where would you go? ')
    responses[name] = response

    restart = input('Would you like to let another person respond? (yes/no) ')

    if restart == 'no':
        poll_active = False


for name, response in responses.items():
    print(f'\n{name.title()} would like to visit {response.title()}.')
