from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverse_linked_list(self, head):
        prev = None
        current = head

        while current is not None:
            new_node = current.next

            current.next, prev = prev, current

            current = new_node

        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:

        # Step 1: Find the middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half
        second_half = self.reverse_linked_list(slow.next)

        # Break the connection between the two halves
        slow.next = None

        # Step 3: Merge the two halves
        first_half = head

        while first_half and second_half:

            first_next = first_half.next
            second_next = second_half.next

            first_half.next = second_half
            second_half.next = first_next

            first_half = first_next
            second_half = second_next


# -----------------------------
# Helper functions for VS Code
# -----------------------------

def create_linked_list(values):
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


def print_linked_list(head):
    current = head

    while current:
        print(current.val, end="")

        if current.next:
            print(" → ", end="")

        current = current.next

    print()


# -----------------------------
# Test
# -----------------------------

values = [1, 2, 3, 4, 5]

head = create_linked_list(values)

print("Before:")
print_linked_list(head)

solution = Solution()
solution.reorderList(head)

print("After:")
print_linked_list(head)