def city_country(city, country):
    full_address = f'"{city.title()}, {country.title()}"'
    return full_address

city = input("Enter the name of the city: ")
country = input("Enter the name of the country: ")

print(city_country(city, country))