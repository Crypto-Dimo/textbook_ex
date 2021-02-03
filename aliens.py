alien_0 = {'color': 'green', 'points': 5,}
alien_1 = {'color': 'yellow', 'points': 10,}
alien_2 = {'color': 'red', 'points': 15,}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print("\n")

# generating aliens

aliens_2 = []

# make 30 aliens

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow',}
    aliens_2.append(new_alien)

# change colors to aliens 

for alien in aliens_2[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

# show the first 5 aliens

for alien in aliens_2[:5]:
    print(alien)
print("...")

print(f"The total number of aliens is: {len(aliens_2)}")




