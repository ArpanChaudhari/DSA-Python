from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # If there is only one node,
        # deleting the middle means deleting the only node.
        if head.next is None:
            return None

        prev = None
        slow = head
        fast = head

        # Find middle node
        # prev will point to the node before middle
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Delete the middle node
        prev.next = slow.next

        return head


# --------------------------------
# Helper: Create Linked List
# --------------------------------

def create_linked_list(values):
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


# --------------------------------
# Helper: Print Linked List
# --------------------------------

def print_linked_list(head):
    current = head

    while current:
        print(current.val, end="")

        if current.next:
            print(" → ", end="")

        current = current.next

    print()


# --------------------------------
# Test
# --------------------------------

values = [1, 2, 3, 4, 5]

head = create_linked_list(values)

print("Before:")
print_linked_list(head)

solution = Solution()

head = solution.deleteMiddle(head)

print("After:")
print_linked_list(head)