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
    def removeDuplicates(self, head):
        if head is None:
            return None

        left = head
        right = head.next

        while right:
            if right.val != left.val:
                left.next = right
                right.prev = left

                left = right
            
            right = right.next

        left.next = None
        
        return head


arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]

# Create doubly linked list
dll = DoublyLinkedList()

# Insert array values
dll.insert_from_array(arr)

# Display linked list
print("Doubly Linked List:")
dll.display()

# Find pairs
solution = Solution()
result = solution.removeDuplicates(dll.head)

print("\nDoubly Linked List after removing duplicates:")
dll.display()