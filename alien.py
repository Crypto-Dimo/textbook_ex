# adding a key to a dictionary

alien_0 = {'speed': 'medium'}

alien_0['x_position'] = 0
alien_0['y_position'] = 25


alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

# removing a key from dictionary

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

del alien_0['speed']

# use get() to access values

point_value = alien_0.get('x_position')

point_value_error = alien_0.get('points', 'No points value assigned.')

print(point_value)
print(point_value_error)