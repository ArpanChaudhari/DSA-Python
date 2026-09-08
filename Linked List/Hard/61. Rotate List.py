# Definition for singly-linked list
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution 1
# class Solution:

    # Get kth node
    def getKthNode(self, node, k):
        k -= 1

        while node and k > 0:
            node = node.next
            k -= 1

        return node

    # Reverse Linked List
    def reverseLL(self, head):
        prev = None
        curr = head

        while curr:
            new_node = curr.next

            curr.next = prev
            prev = curr

            curr = new_node

        return prev

    # Rotate Linked List Right by k
    def rotateRight(self, head, k):

        if head is None or head.next is None:
            return head

        # Find length
        n = 0
        temp = head

        while temp:
            n += 1
            temp = temp.next

        # Avoid unnecessary rotations
        k = k % n

        if k == 0:
            return head

        # 1. Reverse whole linked list
        head = self.reverseLL(head)

        # Example:
        # Original: 1 -> 2 -> 3 -> 4 -> 5
        # Reversed: 5 -> 4 -> 3 -> 2 -> 1

        temp = head

        # 2. Find kth node
        kthNode = self.getKthNode(temp, k)

        # 3. Disconnect after kth node
        second = kthNode.next
        kthNode.next = None

        # 4. Reverse both parts
        first = self.reverseLL(temp)
        second = self.reverseLL(second)

        # 5. Connect both parts
        temp.next = second

        return first

# Solution 2
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        # Find length & Last Node
        n = 1
        tail = head

        while tail.next:
            n += 1
            tail = tail.next

        k = k % n

        if k == 0:
            return head

        # Make Circular LL
        tail.next = head
        
        # Find New tails
        step = n - k
        new_tail = head

        for _ in range(step-1):
            new_tail = new_tail.next
        
        # New head is after new_tail
        new_head = new_tail.next

        # Break Circle
        new_tail.next = None 

        return new_head

    
# Linked List Helper Functions

def insertFromArray(arr):

    if not arr:
        return None

    head = ListNode(arr[0])
    temp = head

    for i in range(1, len(arr)):
        new_node = ListNode(arr[i])

        temp.next = new_node
        temp = new_node

    return head


def display(head):

    temp = head

    while temp:
        print(temp.val, end=" -> ")
        temp = temp.next

    print("None")


# ==================================================
# Main
# ==================================================

arr = [1, 2, 3, 4, 5]
k = 2

# Create Linked List
head = insertFromArray(arr)

print("Original Linked List:")
display(head)

# Rotate Linked List
solution = Solution()
head = solution.rotateRight(head, k)

print("\nAfter Rotating Right by", k, "positions:")
display(head)