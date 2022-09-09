#Dictionary, Set and Tuple
from logging import root
from year import Year
from fruits import FruitBasket
from users import UserProfile
from family import FamilyMember
from linked_list import LinkedList
from binary_node import BinaryNode

#Tuple - Refer to year module
#p = Year()
#p.find_pi_day()

#Set - Refer to fruits module
#fb = FruitBasket()

# fb.add_fruit("Apple")
# fb.add_fruit("Watermelon")
# fb.display_fruits()


#Dictionary - Refer to users module
#u_mw = UserProfile("Matthew", "Walloch", "matthewrwalloch@gmail.com", "999-999-9999")
#u_mw.display_profile()



#List of Dictionaries
# my_family = {
#     "1" : FamilyMember("Robert", "Walloch", "father"),
#     "2" : FamilyMember("Rose", "Walloch", "mother"),
#     "3" : FamilyMember("Katelyn", "Walloch", "sister")
# }

# for key, value in my_family.items():
#     my_family[key].introduce_family()
    


#Linked List
#my_linked_list = LinkedList()
# my_linked_list.append_node(20)
# my_linked_list.append_node(30)
# my_linked_list.append_node(40)
# my_linked_list.append_node(50)
# my_linked_list.append_node(60)

# print(my_linked_list.find_node(123))
# print(my_linked_list.find_node(40))


#BST
root = BinaryNode(27)
root.insert_node(14)
root.insert_node(40)
root.insert_node(35)
root.insert_node(45)
root.insert_node(1)

print(root.search_for_node(root, 35))
print(root.search_for_node(root, 13))
