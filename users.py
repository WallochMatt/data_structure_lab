class UserProfile:
    def __init__(self, first_name, last_name, email, phone):
            self.first_name = first_name
            self.last_name = last_name
            self.email = email
            self.phone = phone

    def display_profile(self):
        print(f"{self.first_name}" + " " + f"{self.last_name}")
        print(f"{self.email}" + "\n" + f"{self.phone}")