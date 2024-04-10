class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    def add(self, data):
        if(self.root == None):
            self.root = Node(data)
        else:
            current = self.root
            while(True):
                if(current.data > data):
                    if(current.left == None):
                        current.left = Node(data)
                        break
                    current = current.left
                if(current.data < data):
                    if(current.right == None):
                        current.right = Node(data)
                        break
                    current = current.right

    def postOrder(self, node=None):
        global answer

        if node==None:
            node = self.root

        if node.left != None:
            self.postOrder(node.left)
        if node.right != None:
            self.postOrder(node.right)
        answer.append(node.data)



if __name__ == '__main__':
    t = Tree()

    while True:
        try:
            t.add (int(input()))
        except:
            break

    answer = []
    t.postOrder()

