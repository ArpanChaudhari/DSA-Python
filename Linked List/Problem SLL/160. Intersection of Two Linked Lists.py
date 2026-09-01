from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: Optional[ListNode], headB: Optional[ListNode]
    ) -> Optional[ListNode]:

        temp1 = headA
        temp2 = headB

        while temp1 != temp2:
            temp1 = temp1.next if temp1 else headB
            temp2 = temp2.next if temp2 else headA

        return temp1


# Function to display linked list
def displayLinkedList(head):
    temp = head

    while temp:
        print(temp.val, end=" -> ")

        temp = temp.next

    print("None")


# ---------------- TEST CODE ----------------

# Create common/intersection part
common1 = ListNode(2)
common2 = ListNode(4)

common1.next = common2


# Create List A: 3 -> 2 -> 2 -> 4
headA = ListNode(3)
nodeA = ListNode(2)

headA.next = nodeA
nodeA.next = common1


# Create List B: 1 -> 9 -> 1 -> 2 -> 4
headB = ListNode(1)
nodeB1 = ListNode(9)
nodeB2 = ListNode(1)

headB.next = nodeB1
nodeB1.next = nodeB2
nodeB2.next = common1


# Display both linked lists
print("Linked List A:")
displayLinkedList(headA)

print()

print("Linked List B:")
displayLinkedList(headB)


# Find intersection
solution = Solution()
intersection = solution.getIntersectionNode(headA, headB)


# Print result
if intersection:
    print("\nIntersection Node Value:", intersection.val)
else:
    print("\nNo Intersection")