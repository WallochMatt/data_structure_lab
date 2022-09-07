#Dictionary, Set and Tuple
from year import Year
from fruits import FruitBasket
from users import UserProfile
from family import FamilyMember


#Tuple - Refer to year module
p = Year()
#p.find_pi_day()

#Set - Refer to fruits module
fb = FruitBasket()
# fb.add_fruit("Apple")
# fb.add_fruit("Watermelon")
# fb.display_fruits()


#Dictionary - Refer to users module
u_mw = UserProfile("Matthew", "Walloch", "matthewrwalloch@gmail.com", "999-999-9999")
#u_mw.display_profile()



#List of Dictionaries
my_family = {
    "1" : FamilyMember("Robert", "Walloch", "father"),
    "2" : FamilyMember("Rose", "Walloch", "mother"),
    "3" : FamilyMember("Katelyn", "Walloch", "sister")
}

# for key, value in my_family.items():
#     my_family[key].introduce_family()
    
