from typing import Optional


# ---------------------------------------
# Definition for singly-linked list
# ---------------------------------------

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # -----------------------------------
    # Main Merge Sort Function
    # -----------------------------------

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Base case
        # If list has 0 or 1 node, it is already sorted
        if head is None or head.next is None:
            return head

        # Step 1: Find the middle
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow


        # Step 2: Split into two linked lists
        left_head = head
        right_head = mid.next
        mid.next = None

        # Step 3: Recursively sort left half
        left_head = self.sortList(left_head)

        # Step 4: Recursively sort right half
        right_head = self.sortList(right_head)

        # Step 5: Merge both sorted lists

        return self.merge(left_head,right_head)


    # -----------------------------------
    # Merge Two Sorted Linked Lists
    # -----------------------------------

    def merge(self, list1, list2):

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
        
        # Attach remaining sorted nodes
        curr.next = t1 if t1 else t2

        return dummy.next


# ---------------------------------------
# Helper: Create Linked List
# ---------------------------------------

def create_linked_list(values):

    if not values:
        return None

    head = ListNode(values[0])
    curr = head

    for value in values[1:]:
        curr.next = ListNode(value)
        curr = curr.next

    return head


# ---------------------------------------
# Helper: Print Linked List
# ---------------------------------------

def print_linked_list(head):

    curr = head

    while curr:
        print(curr.val, end="")

        if curr.next:
            print(" → ", end="")

        curr = curr.next

    print()


# ---------------------------------------
# Test
# ---------------------------------------

values = [4, 2, 1, 3]

head = create_linked_list(values)

print("Before Sorting:")
print_linked_list(head)


solution = Solution()

head = solution.sortList(head)


print("After Sorting:")
print_linked_list(head)