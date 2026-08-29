from typing import Optional


# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy

        t1 = list1
        t2 = list2

        while t1 and t2:

            if t1.val <= t2.val:
                curr.next = t1
                curr = curr.next
                t1 = t1.next
            else:
                curr.next = t2
                curr = curr.next
                t2 = t2.next

        while t1:
            curr.next = t1
            t1 = t1.next

        while t2:
            curr.next = t2
            t2 = t2.next

        return  dummy.next


# ---------------------------------------
# Helper: Create Linked List
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
# Helper: Print Linked List
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

list1_values = [1, 2, 4]
list2_values = [1, 3, 4]

list1 = create_linked_list(list1_values)
list2 = create_linked_list(list2_values)

print("List 1:")
print_linked_list(list1)

print("List 2:")
print_linked_list(list2)


solution = Solution()

result = solution.mergeTwoLists(list1, list2)

print("Merged List:")
print_linked_list(result)
