/**
 * Implementation of a doubly linked list.
 */


/**
 * A node of a doubly linked list contains pointers to
 * next and previous elements, and a key for the value.
 */
class DoublyLinkedListNode{
    public:
        int key;
        DoublyLinkedListNode *next = nullptr;
        DoublyLinkedListNode *prev = nullptr;
};

/**
 * Doubly Linked list implementation.
 * Has methods for searching, insertion and deletion
 */
class DoublyLinkedList{
    public:
        // A constructor with no arguments
        DoublyLinkedList();
        DoublyLinkedListNode* searchForNode(int key);
        void insertNode(DoublyLinkedListNode* node1, DoublyLinkedListNode* node2);
        void insertNodeFront(DoublyLinkedListNode* node);
        void deleteNode(DoublyLinkedListNode* node);
        // The head and tail of the list
        DoublyLinkedListNode *head = nullptr;
        DoublyLinkedListNode *tail = nullptr;
};


/**
 * Search for a node with the given key in the tree.
 * Runtime: O(n) worst case
 * @key: the key of the node to search for.
 * 
 * Return:
 *      a pointer to the node with the given key
 */
DoublyLinkedListNode* DoublyLinkedList::searchForNode(int key){
    DoublyLinkedListNode *temp = head;

    while (temp != nullptr and temp->key != key) {
        temp = temp->next;
    }
    return temp;
}

/**
 * Insert a node anywhere in the tree.
 * Runtime: O(1)
 * @node1: the node to insert in the tree
 * @node2: the node to insert the new node after.
 * 
 * Return:
 *      void
 */
void DoublyLinkedList::insertNode(DoublyLinkedListNode* node1, DoublyLinkedListNode* node2) {
    node1->next = node2->next;
    node1->prev = node2;

    if (node2->next != nullptr) {
        node2->next->prev = node1;
    }
    node2->next = node1;
}

/**
 * Insert a node to the fron of the list.
 * Runtime: O(1)
 * @node: the node to insert in the list
 * 
 * Return:
 *      void
 */
void DoublyLinkedList::insertNodeFront(DoublyLinkedListNode* node) {
    node->next = head;
    node->prev = nullptr;

    if (head != nullptr) {
        head->prev = node;
    }
    head = node;
}

/**
 * Delete a node from the list
 * Runtime: O(1)
 * @node: the node to delete from the list.
 * 
 * Return:
 *      void
 */
void DoublyLinkedList::deleteNode(DoublyLinkedListNode* node) {
    if (node->prev != nullptr) {
        node->prev->next = node->next;
    } else {
        head = node->next;
    }

    if (node->next != nullptr) {
        node->next->prev = node->prev;
    }
}
