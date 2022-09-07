#Dictionary, Set and Tuple

#Tuple
months_of_the_year = (
    "January", "February", "March", "April",
     "May", "June", "July", "August", 
     "September", "October", "November", "December"
     )
#print(months_of_the_year[(int(3.14) - 1)])


#Set
a_set_of_fruits = {"Banana", "Blueberry", "Raspberry", "Pear", "Orange"}

a_set_of_fruits.add("Apple")
a_set_of_fruits.add("Watermelon")

def display_fruits(collection_of_fruit):
    """
    Parameter:
    A colllection : {} or [] -> Any iterable collection, primarily fruit
    
    Prints to the console
    """
    for fruit in collection_of_fruit:
        print(fruit)
#display_fruits(a_set_of_fruits)


#Dictionary
def create_user(first_name, last_name, email, phone):
    """
    Pararmeter:
    Takes str of First name, Last name, email, and phone number

    Returns
    user_info in the form of a dictionary
    """
    user_info = {
        "First Name" : first_name,
        "Last Name" : last_name,
        "Email Address" : email,
        "Phone Number" : phone
    }
    return user_info

user_walloch = (create_user("Matthew", "Walloch", "matthewrwalloch@gmail.com", "999-999-9999"))
#your_user = (create_user())

def display_profile(user_information):
    """
    Parameter:
    user_information : variable = create_user() -> The user who's info you want to print
    """
    print(f"{user_information['First Name']}" + " " + f"{user_information['Last Name']}")
    print(f"{user_information['Email Address']}" + "\n" + f"{user_information['Phone Number']}")

display_profile(user_walloch)





#List of Dictionaries