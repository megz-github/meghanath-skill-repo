sandwich_ord = ['turkey', 'ham and cheese', 'veggie', 'tuna', 'pastrami', 'chicken', 'pastrami', 'pastrami']

# Make an empty list for finished sandwiches
finished_sandwiches = []

# Print a message about running out of pastrami
print("Sorry, the deli has run out of pastrami.\n")

# Remove all occurrences of 'pastrami' from sandwich_orders using a while loop
while 'pastrami' in sandwich_ord:
    sandwich_ord.remove('pastrami')

# Loop through the list of sandwich orders
while sandwich_ord:
    current_order = sandwich_ord.pop(0)
    
    if current_order != 'pastrami':
        print(f"I made your {current_order} sandwich.")
        # Move the made sandwich to the list of finished sandwiches
        finished_sandwiches.append(current_order)

# Print a message listing each sandwich that was made
print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich} sandwich")
