from hmac import new


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
        
        print(f"Node with data {data} created")
        print(f"Node {self.data} updated with a left {self.left} and a right of {self.right}")
        #return new_node

    def search_for_node(self, value_searching_for):
        pass

#