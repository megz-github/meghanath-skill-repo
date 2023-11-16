"""Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the

owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about 

each pet"""

pet1 = {'animal': 'Dog', 'owner': 'Alice'}
pet2 = {'animal': 'Cat', 'owner': 'Bob'}
pet3 = {'animal': 'Bird', 'owner': 'Charlie'}

# Storing the pet dictionaries in a list called pets
pets = [pet1, pet2, pet3]

# Loop through the list and print information about each pet
for pet in pets:
    print(f"Animal: {pet['animal']}")
    print(f"Owner: {pet['owner']}")
    print()  # Print a blank line for separation
