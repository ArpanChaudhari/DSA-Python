class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert values from an array
    def insert_from_array(self, arr):
        for value in arr:
            new_node = ListNode(value)

            if self.head is None:
                self.head = new_node
            else:
                temp = self.head

                while temp.next:
                    temp = temp.next

                temp.next = new_node
                new_node.prev = temp

    # Display the linked list
    def display(self):
        temp = self.head

        while temp:
            print(temp.val, end=" <-> ")
            temp = temp.next

        print("None")


class Solution:
    def findPairsWithGivenSum(self, head, target):
        ans = []

        # left pointer
        left = head

        # right pointer: move to the last node
        right = head

        while right.next:
            right = right.next

        # Two pointer approach
        while left != right and left.prev != right:

            total = left.val + right.val

            if total == target:
                ans.append([left.val, right.val])

                left = left.next
                right = right.prev

            elif total < target:
                left = left.next

            else:
                right = right.prev

        return ans


arr = [1, 2, 3, 4, 5, 6]
target = 7

# Create doubly linked list
dll = DoublyLinkedList()

# Insert array values
dll.insert_from_array(arr)

# Display linked list
print("Doubly Linked List:")
dll.display()

# Find pairs
solution = Solution()
result = solution.findPairsWithGivenSum(dll.head, target)

print("\nPairs with sum", target, ":")
print(result)