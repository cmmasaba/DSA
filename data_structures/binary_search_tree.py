"""Implementation of a Binary Search Tree data structure.
Has the following methods:
- Search
- Insert
- Delete
- Minimum and Maximum
- Predecessor and Successor
"""

class Node:
    def __init__(self, parent=None, right=None, left=None, key=None) -> None:
        self.parent = parent
        self.right = right
        self.left = left
        self.key = key

class BST:
    def __init__(self, root: Node = None):
        self.root = root

    def __inorder_tree_walk(self, temp: Node):
        if temp:
            self._BST__inorder_tree_walk(temp.left)
            print(temp.key)
            self._BST__inorder_tree_walk(temp.right)

    def print_tree(self):
        if self.root is None:
            print("Empty tree")
            return
        return self._BST__inorder_tree_walk(self.root)

    def search(self, node: Node, val):
        x = node
        while x and x.key != val:
            if val < x.key:
                x = x.left
            else:
                x = x.right
        return x

    @property
    def minimum(self):
        temp = self.root
        while temp.left:
            temp = temp.left
        return temp

    @property
    def maximum(self):
        temp = self.root
        while temp.right:
            temp = temp.right
        return temp

    def successor(self, node: Node):
        if node.right:
            return self.minimum(node.right)
        else:
            parent = node.parent
            while parent and node == parent.right:
                parent, node = node, parent.parent
            return parent

    def predecessor(self, node: Node):
        if node.left:
            return self.maximum(node.left)
        else:
            parent = node.parent
            while parent and node == parent.left:
                parent, node = parent, parent.parent
            return parent

    def insert(self, node: Node):
        temp = self.root
        parent = None

        while temp:
            parent = temp
            if node.key < temp.key:
                temp = temp.left
            else:
                temp = temp.right

        node.parent = parent
        if parent is None:
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node

    def delete(self, node: Node):
        if node.left is None:
            self.__transplant(node, node.right)
        elif node.right is None:
            self.__transplant(node, node.left)
        else:
            temp = self.minimum(node.right)
            if temp != node.right:
                self.__transplant(temp. temp.right)
                temp.right = node.right
                temp.right.parent = temp
            self.__transplant(node, temp)
            temp.left = node.left
            temp.left.parent = temp


    def __transplant(self, node1: Node, node2: Node):
        if node1.parent is None:
            self.root = node2
        elif node1 == node1.parent.left:
            node1.parent.left = node2
        else:
            node1.parent.right = node2

        if node2:
            node2.parent = node1.parent


tree = BST()

def populate_tree():
    import random
    seed = random.randint(1, 1000)
    random.seed(seed)

    vals = [random.randint(1, 100) for _ in range(10)]
    for i in vals:
        temp = Node(key=i)
        tree.insert(temp)

populate_tree()
tree.print_tree()
print(f"Root: {tree.root.key}")
print(f"Minimum: {tree.minimum.key}")
print(f"Maximum: {tree.maximum.key}")