# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # Reverse complete linked list
    def reverseLL(self, head):
        prev = None
        curr = head

        while curr:
            new_node = curr.next

            curr.next, prev = prev, curr

            curr = new_node

        return prev

    # Get kth node from current node
    def getkthNode(self, node, k):
        k -= 1

        while node and k > 0:
            node = node.next
            k -= 1

        return node

    # Reverse linked list in groups of k
    def reverseKGroup(self, head, k):

        temp = head
        prevLast = None  # Used to connect previous group

        while temp:

            # Find kth node
            kthNode = self.getkthNode(temp, k)

            # Less than k nodes remain
            if kthNode is None:

                if prevLast:
                    prevLast.next = temp

                break

            # Store next group starting node
            nextNode = kthNode.next

            # Separate current group
            kthNode.next = None

            # Reverse current group
            self.reverseLL(temp)

            # Connect reversed group
            if temp == head:
                # First group
                head = kthNode

            else:
                # Remaining groups
                prevLast.next = kthNode

            # temp is now the last node of reversed group
            prevLast = temp

            # Move to next group
            temp = nextNode

        return head


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


arr = [1, 2, 3, 4, 5, 6, 7, 8]
k = 3

# Create linked list from array
head = insertFromArray(arr)

print("Original Linked List:")
display(head)

# Reverse in groups of k
solution = Solution()
head = solution.reverseKGroup(head, k)

print("\nAfter Reverse in Groups of", k, ":")
display(head)