def desc_city(city, country="default country"):
    description = f"{city} is in {country}."
    print(description)

# Call the function for three different cities
desc_city("Reykjavik", "Iceland")
desc_city("Paris", "France")
desc_city("New York")  # This will use the default country
