prompt = "Enter a message and I will repeat it to you: "

message = " "

while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

# using the 'flag' variable

prompt = "Enter a message and I will repeat it to you: "

# active is the variable used in this case as flag

active = True

while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(message)
