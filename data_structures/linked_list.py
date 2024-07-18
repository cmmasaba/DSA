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

class SinglyLinkedList:
    """Representation of a singly linked list"""
    def __init__(self, head = None):
        """
        Args:
            head: the Node of the first element in the list, initialized to zero.
        """
        self.head = head
    
    def insert_beginning(self, value):
        """Insert a new Node at the beginning of the list.
        
        Args:
            value: the value to be stored in the new Node.
        """
        # create a new Node, assign the current head Node to be next on the new Node. set the head to the new Node
        new_head = SinglyNode(value)
        new_head.next = self.head
        self.head = new_head
    
    def insert_middle(self, previous: SinglyNode, value):
        """Insert a new node in the middle of the list after the provided previous Node.
        
        Args:
            previous: the Node to insert the new Node after.
            value: the value to be stored in the new Node.
        """
        assert isinstance(previous, SinglyNode)

        # create a new Node, assign new Node's next to the previous's next, and assign previous's next to new Node
        new_node = SinglyNode(value)
        new_node.next = previous.next
        previous.next = new_node
    
    def insert_end(self, value):
        """Insert a new Node to the end of the list.
        
        Args:
            value: the value to be stored in the Node.
        """
        new_node = SinglyNode(value)

        # if the list is empty, add the Node to be the head
        if self.head == None:
            self.head = new_node
        else:
            # the list is not empty
            last = self.head
            while last.next:
                # iterate until the last node which points to None
                last = last.next
            
            last.next = new_node

    def delete_head(self):
        """Delete the first Node in the list."""
        if self.head == None:
            return

        old_head = self.head
        self.head = old_head.next
        del old_head
    
    def delete_tail(self):
        """Delete the last Node in the list."""
        
        if self.head == None:
            return
        
        last = self.head
        while last.next.next:
            # iterate through Nodes in the list and stop at the second to last Node
            last = last.next

        # Delete the next Node which is the last and the set the current Node's next to None, making it the last Node
        del last.next
        last.next = None
    
    def delete_middle(self, previous_node: SinglyNode, node_to_delete: SinglyNode):
        """Delete a node in the middle of the linked list.
        
        Args:
            node_to_delete: the Node to be deleted.
            previous_node: the node right before the Node to be deleted.
        """
        if self.head == None:
            return
        
        previous_node.next = node_to_delete.next
        del node_to_delete
        
