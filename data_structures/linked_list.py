"""Implementation of variants of linked list.
Singly linked list, Doubly linked list, Circular linked list, etc."""

class SinglyNode:
    """Representation of the node used in singly linked lists.
    """
    def __init__(self, value):
        """
        A Node is comprised of the value it holds and a reference to the next value.

        Args:
            value: [int, str] the value held by the Node.
        """
        self.value = value
        self.next: SinglyNode | None = None
    
    def __repr__(self) -> str:
        """Helpful representation."""
        return self.value

class SinglyLinkedList:
    """Representation of a singly linked list"""
    def __init__(self, nodes = None):
        """
        Args:
            nodes: an iterable with the elements to create the nodes of the list with.
        """
        self.head = None

        if nodes is not None:
            node = SinglyNode(nodes.pop(0))
            self.head = node
            for element in nodes:
                node.next = SinglyNode(element)
                node = node.next

    
    def __repr__(self) -> str:
        """Helpful representation."""
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(node.value)
            node = node.next
        nodes.append("None")

        return " -> ".join(nodes)
    
    def __iter__(self):
        """Traversing the list."""
        node = self.head
        while node is not None:
            yield node
            node = node.next
    
    def insert_beginning(self, node: SinglyNode):
        """Insert a new Node at the beginning of the list.
        
        Args:
            node: the new Node.
        """
        # create a new Node, assign the current head Node to be next on the new Node. set the head to the new Node
        node.next = self.head
        self.head = node
    
    def insert_middle(self, previous: SinglyNode, node: SinglyNode):
        """Insert a new node in the middle of the list after the provided previous Node.
        
        Args:
            previous: the Node to insert the new Node after.
            node: the new Node.
        """
        if self.head is None:
            raise Exception("The linked list is empty!!!")

        assert isinstance(previous, SinglyNode)
        assert isinstance(node, SinglyNode)

        # create a new Node, assign new Node's next to the previous's next, and assign previous's next to new Node
        node.next = previous.next
        previous.next = node
    
    def insert_end(self, node: SinglyNode):
        """Insert a new Node to the end of the list.
        
        Args:
            node: the value to be stored in the Node.
        """
        # if the list is empty, add the Node to be the head
        if self.head is None:
            self.head = node
        else:
            # the list is not empty
            for current_node in self:
                pass

            current_node.next = node

    def delete_head(self):
        """Delete the first Node in the list."""
        if self.head is None:
            raise Exception("The list is empty!!!")
        self.head = self.head.next
    
    def delete_tail(self):
        """Delete the last Node in the list."""
        if self.head is None:
            raise Exception("The list is empty!!!")
        
        previous_node = self.head
        for node in self:
            if node.next is None:
                previous_node.next = None
            previous_node = node

    
    def delete_middle(self, previous_node: SinglyNode, target_node: SinglyNode):
        """Delete a node in the middle of the linked list.
        
        Args:
            target_node: the Node to be deleted.
            previous_node: the node right before the Node to be deleted.
        """
        if self.head is None:
            raise Exception("The list is empty!!!")
        
        previous_node.next = target_node.next
        
