from typing import Optional


# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def removeNthFromEnd(
        self,
        head: Optional[ListNode],
        n: int
    ) -> Optional[ListNode]:

        # If there is only one node,
        # removing it will make the list empty.
        if head.next is None:
            return None

        # Dummy node helps us handle the case
        # where the first node needs to be removed.
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        # Move fast pointer n + 1 steps ahead.
        # This creates a gap of n nodes between slow and fast.
        for _ in range(n + 1):
            fast = fast.next

        # Move both pointers until fast reaches the end.
        # slow will then be just before the node to delete.
        while fast:
            slow = slow.next
            fast = fast.next

        # Remove the Nth node from the end.
        slow.next = slow.next.next

        return dummy.next


# ---------------------------------------
# Helper Function: Create Linked List
# ---------------------------------------

def create_linked_list(values):

    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


# ---------------------------------------
# Helper Function: Print Linked List
# ---------------------------------------

def print_linked_list(head):

    current = head

    while current:

        print(current.val, end="")

        if current.next:
            print(" → ", end="")

        current = current.next

    print()


# ---------------------------------------
# Test
# ---------------------------------------

values = [1, 2, 3, 4, 5]
n = 2

head = create_linked_list(values)

print("Before:")
print_linked_list(head)

solution = Solution()

head = solution.removeNthFromEnd(head, n)

print("After:")
print_linked_list(head)