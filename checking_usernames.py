current_users = ['cryptodimo', 'fedefio', 'dimix', 'jackking', 'minus']
new_users = ['ildimo', 'fedefio', 'karamella', 'dimix', 'Ada']

for user in new_users:
    if user in current_users:
        print("Username already in use, please try another one.")
    else:
        print("The username is available.")
