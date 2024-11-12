"""
A red-black tree is a BST with the following properties:
    1. Every node is either red or black
    2. The root is black
    3. Every leaf is black
    4. If a node is red then both its children must be black.
    5. For each node, all simple paths from the mode to the descendant leaves
       contain the same number of black nodes.
Black height: the number of black nodes on any simple path from, but not including,
              a node x down to a leaf.
"""

from enum import Enum

class NodeColor(Enum):
    """Representation for the possible colors of the nodes in a red-black tree."""
    BLACK = "black"
    RED = "red"

class Node:
    """Representation for the nodes in the red-black tree."""
    def __init__(self, parent = None, right = None, left = None, key = None, color = None) -> None:
        self.parent: Node = parent
        self.right: Node = right
        self.left: Node = left
        self.key = key
        self.color = color

class RB_BST:
    """Implemetation of the methods of a red-black tree."""
    def __init__(self, root: Node = None) -> None:
        self.root = root
        self.nil = Node(color=NodeColor.BLACK)
    
    @property
    def minimum(self, node: Node = None):
        """Find the minimum value in the tree.
        Returns:
            the minimum node.
        """
        if node is not None:
            temp = node
        else:
            temp = self.root

        while temp.left:
            temp = temp.left
        return temp

    @property
    def maximum(self, node: Node = None):
        """Find the maximum value in the tree.
        
        Returns:
            the maximum node.
        """
        if node is not None:
            temp = node
        else:
            temp = self.root

        while temp.right:
            temp = temp.right
        return temp

    def successor(self, node: Node):
        """Find the immediate largest value after node's value.
        
        Args:
            node: the node to find the successor of.
            Returns:
            the successor node.
        """
        if node.right:
            return self.minimum(node.right)
        else:
            parent = node.parent
            while parent and node == parent.right:
                parent, node = node, parent.parent
            return parent

    def predecessor(self, node: Node):
        """Find the immediate smallest value after node's value.
        
        Args:
            node: the node to find the predecessor of.
        Returns:
            the predecessor node.
        """
        if node.left:
            return self.maximum(node.left)
        else:
            parent = node.parent
            while parent and node == parent.left:
                parent, node = node, parent.parent
            return parent
    
    def transplant(self, node_1: Node, node_2: Node):
        """Replace the subtree rooted at node 1 with the subtree rooted at node 2.
        
        Args:
            node_1: a node in the tree.
            node_2: a node in the tree.
        """
        if node_1.parent is self.nil:
            self.root = node_2
        elif node_1 is node_1.parent.left:
            node_1.parent.left = node_2
        else:
            node_1.parent.right = node_2
        node_2.parent = node_1.parent

    def left_rotate(self, node: Node):
        """Runs in O(1) time and changes the pointer structure of the
        red-black tree.

        Args:
            node: the node to perform a left rotation on.
        """
        right_child: Node = node.right
        node.right = right_child.left           # turn right child's left subtree into node's right subtree

        
        if right_child.left is not self.nil:    # if the left subtree isn't empty, make node the parent of the subtree's root.        
            right_child.left.parent = node

        right_child.parent = node.parent        # node's parent becomes right child's parent
        if node.parent is self.nil:             # If node was the root, the right child becomes the root
            self.root = right_child
        elif node is node.parent.left:          # If node is a left child make right child the left child of the parent
            node.parent.left = right_child
        else:                                   # If node is a right child make right child the right child of the parent
            node.parent.right = right_child

        right_child.left = node                 # Make node right child's left child.
        node.parent = right_child


    def right_rotate(self, node: Node):
        """Runs in O(1) time and changes the pointer structure of the
        red-black tree.

        Args:
            node: the node to perform a right rotation on.
        """
        left_child: Node = node.left
        node.left = left_child.right            # turn left child's right subtree into node's left subtree

        if left_child.right is not self.nil:    # if the right subtree isn't empty, make node the parent of the subtree's root.       
            left_child.right.parent = node

        left_child.parent = node.parent         # node's parent becomes left child's parent

        if node.parent is self.nil:             # If node was the root, the left child becomes the root
            self.root = left_child
        elif node is node.parent.right:         # If node is a right child make left child the right child of the parent
            node.parent.right = left_child
        else:                                   # If node is a left child make left child the left child of the parent
            node.parent.left = left_child


        left_child.right = node                 # Make node right child's left child.
        node.parent = left_child
    
    def insert(self, node: Node):
        """Insert the new node into the tree then color it red.
        Call the auxiliary procedure to restore any violated red-
        black tree properties.
        Runtime: O(lg n)
        
        Args:
            node: the node being inserted into the tree."""
        temp_1, temp_2 = self.root, self.nil

        while temp_1 is not self.nil:                                           # Descend until reaching the sentinel.
            if node.key < temp_1.key:
                temp_2, temp_1 = temp_1, temp_1.left
            else:
                temp_2, temp_1 = temp_1, temp_1.right
        node.parent = temp_2

        if temp_2 is self.nil:                                                  # The tree was empty
            self.root = node
        elif node.key < temp_2.key:
            temp_2.left = node
        else:
            temp_2.right = node

        node.left, node.right, node.color = self.nil, self.nil, NodeColor.RED   # Set the node's children to sentinel and color it red.

        self.insert_fixup(node)                                                 # Fix any red-black tree violations.
    
    def insert_fixup(self, node: Node):
        """Fix any violations of the red-black tree properties
        that arise during insertion.
        Runtime: O(lg n)
        
        Args:
            node: the node that was inserted.
        """
        while node.parent.color == NodeColor.RED:
            if node.parent is node.parent.parent.left:      # node's parent is a left child.

                temp: Node  = node.parent.parent.right      # temp is node's uncle

                if temp.color == NodeColor.RED:             # node's parent and uncle both red
                    node.parent.color = NodeColor.BLACK
                    temp.color = NodeColor.BLACK
                    node.parent.parent.color = NodeColor.RED
                    node = node.parent.parent
                else:
                    if node is node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = NodeColor.BLACK
                    node.parent.parent.color = NodeColor.RED
                    self.right_rotate(node.parent.parent)
            else:                                           # node's parent is a right child
                temp = node.parent.parent.left
                if temp.color == NodeColor.RED:
                    node.parent.color = NodeColor.BLACK
                    temp.color = NodeColor.BLACK
                    node.parent.parent = NodeColor.RED
                    node = node.parent.parent
                else:
                    if node is node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = NodeColor.BLACK
                    node.parent.parent.color = NodeColor.RED
                    self.left_rotate(node.parent.parent)
        self.root.color = NodeColor.BLACK
    
    def delete(self, node: Node):
        """Delete a node from the tree.
        
        Args:
            node: the node to be deleted.
        """
        temp_1: Node = node
        temp_1_original_color = temp_1.color
        if node.left is self.nil:
            temp_2 = node.right
            self.transplant(node, node.right)               # Replace node by it's right child
        elif node.right is self.nil:
            temp_2 = node.left
            self.transplant(node, node.left)                # Replace node by it's left child
        else:
            temp_1 = self.minimum(node.right)               # temp_1 is node's successor
            temp_1_original_color = temp_1.color
            temp_2 = temp_1.right
            
            if temp_1 is not node.right:                    # temp_1 is further down the tree
                self.transplant(temp_1, temp_1.right)       # Replace temp_1 by its right child
                temp_1.right = node.right
                temp_1.right.parent = temp_1                # node's right child becomes temp_1's right child
            else:                                           # In case temp_2 is sentinel
                temp_2.parent = temp_1

            self.transplant(node, temp_1)                   # Replace node by it's successor temp_1
            temp_1.left = node.left                         # Give node's left child to temp_1, which had not left child.
            temp_1.left.parent = temp_1
            temp_1.color = node.color

            if temp_1_original_color == NodeColor.BLACK:    # Correct any red-black tree properties violations
                self.delete_fixup(temp_2)


    def delete_fixup(self, node: Node):
        """Restore the red-black tree properties after deletion.
        
        Args:
            node: the node violating red-black tree properties.
        """
        while node is not self.root and node.color == NodeColor.BLACK:
            if node is node.parent.left:        # node is a left child
                temp = node.parent.right
                if temp.color == NodeColor.RED:
                    temp.color = NodeColor.BLACK
                    node.parent.color = NodeColor.RED
                    self.left_rotate(node.parent)
                    temp = node.parent.right
                
                if temp.left.color == NodeColor.BLACK and temp.right.color == NodeColor.BLACK:
                    temp.color = NodeColor.RED
                    node = node.parent
                else:
                    if temp.right.color == NodeColor.BLACK:
                        temp.left.color = NodeColor.BLACK
                        temp.color = NodeColor.RED
                        self.right_rotate(temp)
                        temp = node.parent.right
                    temp.color = node.parent.color
                    node.parent.color = NodeColor.BLACK
                    temp.right.color = NodeColor.BLACK
                    self.left_rotate(node.parent)
                    node = self.root
            else:                               # node is a right child
                temp = node.parent.left
                if temp.color == NodeColor.RED:
                    temp.color = NodeColor.BLACK
                    node.parent.color = NodeColor.RED
                    self.right_rotate(node.parent)
                    temp = node.parent.left
                
                if temp.right.color == NodeColor.BLACK and temp.left.color == NodeColor.BLACK:
                    temp.color = NodeColor.RED
                    node = node.parent
                else:
                    if temp.left.color == NodeColor.BLACK:
                        temp.right.color = NodeColor.BLACK
                        temp.color = NodeColor.RED
                        self.left_rotate(temp)
                        temp = node.parent.left
                    temp.color = node.parent.color
                    node.parent.color = NodeColor.BLACK
                    temp.left.color = NodeColor.BLACK
                    self.right_rotate(node.parent)
                    node = self.root
        
        node.color = NodeColor.BLACK

