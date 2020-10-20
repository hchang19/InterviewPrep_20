class Child:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("I have set the value")
    
    def printInfo(self):
        self.printName()
        self.printAge()
    
    def printName(self):
        print(self.name)
    
    def printAge(self):
        print(self.age)
    
    def sayGibberish(self):
        if(len(self.name) == 0):
            return 
        
        print(self.name)
        self.name = self.name[:-1]
        self.sayGibberish()

from collections import deque 

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    
    def serialize(self, root: TreeNode) -> str:
        encoded_data = []

        self.helpSerialize(root, encoded_data)
        return ' '.join(map(str, encoded_data))
    
    def helpSerialize(self, root:TreeNode, encoded_data: list) -> None:
        if(root is None):
            return
        else:
            encoded_data.append(root.val)
            self.helpSerialize(root.left, encoded_data)
            self.helpSerialize(root.right, encoded_data)
        return

    def deserialize(self, data:str) -> TreeNode:
        """
        decodes data and reconstruct tree
        """
        # data = deque(map(int,data.strip(' ')))
        
        data = deque(map(int, data.split(' ')))
        return self.helpDeserialize(data, -1, 100000)
        
    def helpDeserialize(self, data:deque, lowerbound, upperbound) -> TreeNode:
        if(len(data) == 0):
            return None
        
        if(lowerbound < data[0] < upperbound):
            curr_val = data.popleft()
            node = TreeNode(curr_val)
            node.left = self.helpDeserialize(data, lowerbound, curr_val)
            node.right = self.helpDeserialize(data, curr_val, upperbound)
            return node
        
        

root_node = TreeNode(1)
left_node = TreeNode(0)
right_node = TreeNode(2)

root_node.left = left_node
root_node.right = right_node

def printTree(root: TreeNode) -> None:
    if(root is None):
        return
    else:
        printTree(root.left)
        print(root.val)
        printTree(root.right)

testCodec = Codec()
compressed_tree = testCodec.serialize(root_node)
print(compressed_tree)
printTree(testCodec.deserialize(compressed_tree))