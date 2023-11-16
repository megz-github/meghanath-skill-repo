sandwich_ord = ['turkey', 'ham and cheese', 'veggie', 'tuna', 'chicken']
finished_sandwiches = []
# Loop through the list of sandwich orders
while sandwich_ord:
    current_order = sandwich_ord.pop(0)
    print(f"I made your {current_order} sandwich.")
    
    # Move the made sandwich to the list of finished sandwiches
    finished_sandwiches.append(current_order)
print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich} sandwich")
