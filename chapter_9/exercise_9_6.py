#Exercise 9.6
class Restaurant:
    """A simple class for a restaurant."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """Print the two informations about the restaurant."""
        print(f"The restaurant's name is {self.restaurant_name} and its cuisine type is {self.cuisine_type}.")
    
    def open_restaurant(self):
        """Open the restaurant for bussiness."""
        print("The restaurant is now open!")
    
    def people_served(self, number_served):
        """Refresh the number of people served in the restaurant"""
        self.people_served = number_served
        return self.people_served
    
    def refresh_served(self, number_served):
        """Increment the number of people served"""
        self.people_served = self.people_served + number_served
        return self.people_served

class IceCreamStand(Restaurant):
    """An ice cream stand class"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the child class"""
        super().__init__(restaurant_name, cuisine_type)
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def display_flavors(self, flavors):
        """Display the flavors of the ice cream stand"""
        
        print(f"The following flavors are available at the ice cream stand: ")
        
        for flavor in flavors:
            print(f"- {flavor}")

ice_cream_stand = IceCreamStand('Honey', 'ice cream')
ice_cream_stand.display_flavors(['chocolate', 'strawberry', 'vanila', 'grape'])