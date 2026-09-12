from typing import Optional


# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Base case: If the head is None, return None
        if head is None:
            return None

        # Recursively process the rest of the list
        head.next = self.removeElements(head.next, val)

        # Remove current node if it matches
        if head.val == val:
            return head.next

        return head

# Create linked list from Python list
def create_linked_list(values):
    if not values:
        return None

    head = ListNode(values[0])
    temp = head

    for value in values[1:]:
        temp.next = ListNode(value)
        temp = temp.next

    return head


# Display linked list
def display(head):
    temp = head

    while temp:
        print(temp.val, end="")

        if temp.next:
            print(" -> ", end="")

        temp = temp.next

    print()


val = 6
values = [1, 6, 6, 3]
# Create linked list
head = create_linked_list(values)

print("\nOriginal Linked List:")
display(head)

# Apply solution
solution = Solution()
head = solution.removeElements(head, val)

print("After removing", val, ":")
display(head)