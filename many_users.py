users = {
    'aeinstein': {
        'name': 'albert',
        'surname': 'einstein',
        'city': 'princeton',
        },
    'mcurie': {
        'name': 'marie',
        'surname': 'curie',
        'city': 'paris',
        },
    }

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['name']} {user_info['surname']}"
    location = user_info['city']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
