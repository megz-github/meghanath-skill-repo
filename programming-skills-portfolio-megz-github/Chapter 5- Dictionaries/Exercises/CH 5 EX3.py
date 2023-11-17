"""Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()

calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms 

to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.
"""


programming_glossary = {
    'Variable': 'A named storage location in a programming language.',
    'Function': 'A named section of a program that performs a specific task.',
    'Algorithm': 'A set of well-defined rules for solving a problem.',
    'Loop': 'A programming structure that repeats a sequence of instructions.',
    'Conditional': 'A statement that performs different actions based on whether a condition is true or false.',
    'List': 'An ordered collection of items in Python.',
    'Dictionary': 'A collection of key-value pairs in Python.',
    'Tuple': 'An immutable collection of ordered elements in Python.',
    'Module': 'A file containing Python code that can be used in other programs.',
    'Class': 'A blueprint for creating objects, providing initial values for state (member variables) and implementations of behavior (member functions or methods).'
}

# Printing keys and values using a loop
for term, meaning in programming_glossary.items():
    print(f"{term}:\n{meaning}\n")
