class InvalidCountryException(Exception):
    def __str__(self):
        return ("User Outside India cannot be registered.")

class UserRegistration:
    def registerUser(self, userName, userCountry):
        if (userCountry=="India"):
            print("User registration done successfully.")
        else:
            raise InvalidCountryException

user=UserRegistration()
user.registerUser("Mini","India")
user.registerUser("Mickey","US")
