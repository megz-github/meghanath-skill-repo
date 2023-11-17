"""Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.

* Use a loop to print a sentence about each river, such as The Nile runs through Egypt.

* Use a loop to print the name of each river included in the dictionary.

* Use a loop to print the name of each country included in the dictionary.
"""

# Dictionary of major rivers and the countries they run through
rivers = {
    'Nile': 'Egypt',
    'Yangtze': 'China',
    'Amazon': 'Brazil'
}

# Print a sentence about each river
for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

print("\nList of rivers:")
# Print the name of each river
for river in rivers:
    print(river)

print("\nList of countries:")
# Print the name of each country
for country in rivers.values():
    print(country)
