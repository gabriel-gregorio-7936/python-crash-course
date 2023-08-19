#Exercise 9.1 and 9.2 Restaurant
class Restaurant:
    """A simple class for a restaurant."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """Print the two informations about the restaurant."""
        print(f"The restaurant's name is {self.restaurant_name} and its cuisine type is {self.cuisine_type}.")
    
    def open_restaurant(self):
        """Open the restaurant for bussiness."""
        print("The restaurant is now open!")

restaurant = Restaurant('Omega', 'burguers')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant1 = Restaurant('Divine', 'sea food')
restaurant1.describe_restaurant()

restaurant2 = Restaurant("Angel's Place", 'specialized')
restaurant2.describe_restaurant()