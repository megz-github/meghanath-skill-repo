"""A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

* Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store 

their meanings as values.

* Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print 

the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between 

each word-meaning pair in your output."""

# Creating a glossary of programming terms and their meanings
programming_glossary = {
    'Variable': 'A storage location in a programming language.',
    'Function': 'A section of a program that performs a specific task.',
    'Algorithm': 'A set of well-defined rules for solving a problem.',
    'Loop': 'A structure that repeats a sequence of instructions.',
    'Conditional': 'performs different actions based on whether a condition is true or false.'
}

# Printing each word and its meaning with a blank line between each pair
for term, meaning in programming_glossary.items():
    print(f"{term}:\n{meaning}\n")
