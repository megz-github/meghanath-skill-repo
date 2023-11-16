"""Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping,

print a message saying you’ll add that topping to their pizza."""

while True:
    top = input("Enter a pizza topping (type 'quit' to finish): ")
    
    if top.lower() == 'quit':
        print("Exiting pizza topping selection.")
        break
    
    print(f"Adding {top} to your pizza.")# Additional code can be added here for further processing after the loop.
