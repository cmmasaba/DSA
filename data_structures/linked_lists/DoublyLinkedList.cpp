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
 * 
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

DoublyLinkedListNode* DoublyLinkedList::searchForNode(int key){
    DoublyLinkedListNode *temp = head;

    while (temp != nullptr and temp->key != key) {
        temp = temp->next;
    }
    return temp;
}

void DoublyLinkedList::insertNode(DoublyLinkedListNode* node1, DoublyLinkedListNode* node2) {
    node1->next = node2->next;
    node1->prev = node2;

    if (node2->next != nullptr) {
        node2->next->prev = node1;
    }
    node2->next = node1;
}

void DoublyLinkedList::insertNodeFront(DoublyLinkedListNode* node) {
    node->next = head;
    node->prev = nullptr;

    if (head != nullptr) {
        head->prev = node;
    }
    head = node;
}

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
