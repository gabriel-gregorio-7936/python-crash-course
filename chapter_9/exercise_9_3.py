#Exercise 9.3 and 9.5
class User:
    """Describes and greets an user."""

    def __init__(self, first_name, last_name, profile):
        """Initialize the User class"""
        self.first_name = first_name
        self.last_name = last_name
        self.profile = profile
        self.login_attempts = 0
    
    def describe_user(self):
        """Describe a user."""
        print(f"\nThe user has the following informations: ")
        print(f"His full name is {self.first_name.title()} {self.last_name.title()}.")
        print(f"His profile is {self.profile.title()}")
    
    def greet_user(self):
        """Greet a user."""
        print(f"Hello {self.first_name}!")
    
    def increment_login_attempts(self):
        """Increment the number of login atttempts"""
        self.login_attempts = self.login_attempts + 1
        return self.login_attempts
    
    def reset_login_attempts(self):
        """Reset the number of login attempts"""
        self.login_attempts = 0
        return self.login_attempts

person = User('Kara', 'Montgomery', 'elite')
person.describe_user()
person.greet_user()
print(person.increment_login_attempts())
print(person.increment_login_attempts())
print(person.increment_login_attempts())
print(person.increment_login_attempts())
print(person.increment_login_attempts())
print(person.reset_login_attempts())