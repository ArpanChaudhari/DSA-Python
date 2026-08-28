from typing import Optional


# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # If list has 0 or 1 node
        if head is None or head.next is None:
            return head

        evenHead = evenTail = None
        oddHead = oddTail = None

        count = 1
        curr = head

        while curr is not None:

            # Odd position
            if count % 2 == 1:

                if oddHead is None:
                    oddHead = oddTail = curr
                else:
                    oddTail.next = curr
                    oddTail = curr

            # Even position
            else:

                if evenHead is None:
                    evenHead = evenTail = curr
                else:
                    evenTail.next = curr
                    evenTail = curr

            count += 1
            curr = curr.next

        # Connect odd list with even list
        oddTail.next = evenHead

        # End the linked list
        evenTail.next = None

        return oddHead


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

head = create_linked_list(values)

print("Before:")
print_linked_list(head)

solution = Solution()

head = solution.oddEvenList(head)

print("After:")
print_linked_list(head)