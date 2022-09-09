
class BinaryNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert_node(self, data):
        new_node = BinaryNode(data)

        if (new_node.data > self.data) and self.right is None:
            self.right = new_node

        elif (new_node.data > self.data) and self.right is not None:
            return self.right.insert_node(data)
            #self.right = self.right.insert_node(data)
           # return new_node
                  
        elif (new_node.data < self.data) and self.left is None:
            self.left = new_node
              
        elif (new_node.data < self.data) and self.left is not None:    
            return self.left.insert_node(data)
            #self.left = self.left.insert_node(data)
            #return new_node
        self.text_checker(data, self.data, self.left, self.right)

    def text_checker(self, data, self_data, left_data, right_data):
        if right_data is None:
            right_data = "None"
        else:
            right_data = right_data.data
        if left_data is None:
            left_data = "None"
        else:
            left_data = left_data.data

        print("\n" + f"Node with data {data} created")
        print(f"""Node {self_data} updated with a left {left_data} and a right of {right_data}""")



    def search_for_node(self, root, value_searching_for):
        current_node = root
        print("\n" + f"Searching for node with a value of {value_searching_for}")
        while current_node is not None:
        #if current_node:
            if current_node.data == value_searching_for:
                print("Results:")
                return True
                
            elif current_node.data < value_searching_for:
                current_node = current_node.right
                print("Searching right...")
            
            elif current_node.data > value_searching_for:
                current_node = current_node.left
                print("Searching left...")

        print("Results:")
        return False
