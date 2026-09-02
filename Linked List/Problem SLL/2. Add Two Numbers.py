from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry

            carry = total // 10

            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next


# Create Linked List
def createLinkedList(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


# Display Linked List
def displayLinkedList(head):
    current = head

    while current:
        print(current.val, end=" -> ")
        current = current.next

    print("None")


# Test
l1 = createLinkedList([2, 4, 3])
l2 = createLinkedList([5, 6, 4])

solution = Solution()
result = solution.addTwoNumbers(l1, l2)

print("List 1:")
displayLinkedList(l1)

print("List 2:")
displayLinkedList(l2)

print("Result:")
displayLinkedList(result)