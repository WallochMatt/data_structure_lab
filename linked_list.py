class Node:
    def __init__(self, value):
        self.value = value
        self.pointer = None
        

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_node(self, value_to_add):
        new_node = Node(value_to_add)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        else:
            self.tail.pointer = new_node
            self.tail = self.tail.pointer


    def find_node(self, search_value):
        current_node = self.head
        while current_node is not None: #while ointer is not the tail
            if current_node.value == search_value:
                return print("True")
            else:
                current_node = current_node.pointer    
        return print("False")


