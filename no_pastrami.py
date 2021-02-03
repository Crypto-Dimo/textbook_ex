sandwich_orders = ['pastrami', 'tuna mayo', 'BLT', 'pastrami', 'ham & cheese', 'pastrami', 'chicken pesto']

print('We are sorry but the Deli run out of Pastrami.')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'I made your {sandwich} sandwich.')
    finished_sandwiches.append(sandwich)

print('\n---List of sandwiches---\n')

for sandwich in finished_sandwiches:
    print(f'- {sandwich} sandwich.')