prompt = "Enter the topping for your pizza (enter 'quit' to end the order): "

message = " "

while message != 'quit':
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print(f"You added {message} to your pizza.")