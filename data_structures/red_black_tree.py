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
from copy import deepcopy

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

    def left_rotate(self, node: Node):
        """Runs in O(1) time and changes the pointer structure of the
        red-black tree.

        Args:
            node: the node to perform a left rotation on.
        """
        right_child: Node = node.right
        # turn right child's left subtree into node's right subtree
        node.right = right_child.left

        # if the left subtree isn't empty, make node the parent of
        # the subtree's root.
        if right_child.left is not self.nil:           
            right_child.left.parent = node
        # node's parent becomes right child's parent
        right_child.parent = node.parent
        # If node was the root, the right child becomes the root
        if node.parent is self.nil:
            self.root = right_child
        # If node is a left child make right child the left child
        # of the parent
        elif node is node.parent.left:
            node.parent.left = right_child
        # If node is a right child make right child the right child
        # of the parent
        else:
            node.parent.right = right_child
        
        # Make node right child's left child.
        right_child.left = node
        node.parent = right_child


    def right_rotate(self, node: Node):
        """Runs in O(1) time and changes the pointer structure of the
        red-black tree.

        Args:
            node: the node to perform a right rotation on.
        """
        left_child: Node = node.left
        # turn left child's right subtree into node's left subtree
        node.left = left_child.right

        # if the right subtree isn't empty, make node the parent of
        # the subtree's root.
        if left_child.right is not self.nil:           
            left_child.right.parent = node
        # node's parent becomes left child's parent
        left_child.parent = node.parent
        # If node was the root, the left child becomes the root
        if node.parent is self.nil:
            self.root = left_child
        # If node is a right child make left child the right child
        # of the parent
        elif node is node.parent.right:
            node.parent.right = left_child
        # If node is a left child make left child the left child
        # of the parent
        else:
            node.parent.left = left_child
        
        # Make node right child's left child.
        left_child.right = node
        node.parent = left_child
    
    def insert(self, node: Node):
        """Insert the new node into the tree then color it red.
        Call the auxiliary procedure to restore any violated red-
        black tree properties.
        Runtime: O(lg n)
        
        Args:
            node: the node being inserted into the tree."""
        temp_1, temp_2 = self.root, self.nil

        # Descend until reaching the sentinel.
        while temp_1 is not self.nil:
            if node.key < temp_1.key:
                temp_2, temp_1 = temp_1, temp_1.left
            else:
                temp_2, temp_1 = temp_1, temp_1.right
        node.parent = temp_2

        # The tree was empty
        if temp_2 is self.nil:
            self.root = node
        elif node.key < temp_2.key:
            temp_2.left = node
        else:
            temp_2.right = node

        # Set the node's children to sentinel and color it red.
        node.left, node.right, node.color = self.nil, self.nil, NodeColor.RED

        # Fix any red-black tree violations.
        self.insert_fixup(node)
    
    def insert_fixup(self, node: Node):
        """Fix any violations of the red-black tree properties
        that arise during insertion.
        Runtime: O(lg n)
        
        Args:
            node: the node that was inserted.
        """
        while node.parent.color == NodeColor.RED:
            # node's parent is a left child.
            if node.parent is node.parent.parent.left:
                # temp is node's uncle
                temp: Node  = node.parent.parent.right
                # node's parent and uncle both red
                if temp.color == NodeColor.RED:
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
            # node's parent is a right child
            else:
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
        pass

    def delete_fixup(self, node: Node):
        pass

    def transplant(self, node_1: Node, node_2: Node):
        pass

    @property
    def minimum(self):
        """Find the minimum value in the tree.
        Returns:
            the minimum node.
        """
        temp = self.root
        while temp.left:
            temp = temp.left
        return temp

    @property
    def maximum(self):
        """Find the maximum value in the tree.
        
        Returns:
            the maximum node.
        """
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

