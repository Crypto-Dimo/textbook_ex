sandwich_orders = ['tuna mayo', 'BLT', 'ham & cheese', 'chicken pesto']

finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'I made your {sandwich} sandwich.')
    finished_sandwiches.append(sandwich)

print('\n---List of sandwiches---\n')

for sandwich in finished_sandwiches:
    print(f'- {sandwich} sandwich.')
