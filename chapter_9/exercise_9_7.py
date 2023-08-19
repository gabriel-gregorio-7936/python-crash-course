#Exercise 9.7
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

class Admin(User):
    """A class for the admin user"""
    
    def __init__(self, first_name, last_name, profile):
        """Initialize the class Admin"""
        super().__init__(first_name, last_name, profile)
        self.first_name = first_name
        self.last_name = last_name
        self.profile = profile
        self.privileges = Privileges()

class Privileges:
    """A class for storing the privileges an admin has"""

    def __init__(self, privileges):
        """Initialize the privileges attributes"""
        self.privileges = privileges

    def show_privileges(self, privileges):
        """Show a list of privileges of the Admin"""
        
        print("\nThe Admin has the following privileges: ")

        for privilege in privileges:
            print(f"- {privilege}")

person = User('Kara', 'Montgomery', 'elite')
person.describe_user()
person.greet_user()
print(person.increment_login_attempts())
print(person.increment_login_attempts())
print(person.increment_login_attempts())
print(person.increment_login_attempts())
print(person.increment_login_attempts())
print(person.reset_login_attempts())

admin_person = Admin('Kara', 'Montgomery', 'elite')
#admin_person.show_privileges()
admin_person.privileges.show_privileges(['can add post', 'can delete post', 'can ban user'])