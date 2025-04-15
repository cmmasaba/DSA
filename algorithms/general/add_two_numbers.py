"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself."""

class ListNode:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        carry = 0
        head = ListNode()
        current = head

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sum = val1 + val2 + carry
            digit = sum % 10
            carry = sum // 10

            node = ListNode(val=digit)
            current.next = node
            current = node

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return head.next

def printNode(node):
    result = []
    while node:
        result.append(str(node.val))
        node = node.next
    result.reverse()
    print("".join(result))

def main():
    head1 = ListNode()
    current = head1
    for i in range(1,4):
        node = ListNode(val=i)
        current.next = node
        current = node
    printNode(head1.next)

    head2 = ListNode()
    current = head2
    for i in range(0, 5):
        node = ListNode(val=i)
        current.next = node
        current = node
    printNode(head2.next)

    soln = Solution()
    result = soln.addTwoNumbers(head1.next, head2.next)
    printNode(result)

if __name__ == "__main__":
    main()
