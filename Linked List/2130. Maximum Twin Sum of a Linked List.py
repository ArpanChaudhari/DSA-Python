# Definition for singly-linked list
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def reverseLL(self, head):
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        previous = None
        current = head

        while current:
            next_node = current.next

            # Reverse the link
            current.next, previous = previous, current

            current = next_node

        return previous

    def maximumTwinSum(self):
        # Time Complexity: O(n)
        # Auxiliary Space: O(1)

        if self.head is None or self.head.next is None:
            return 0

        # Step 1: Find the middle using slow and fast pointers
        slow = self.head
        fast = self.head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Split the linked list
        second_half = slow.next
        slow.next = None

        # Step 3: Reverse the second half
        reversed_second = self.reverseLL(second_half)

        # Step 4: Calculate maximum twin sum
        first_half = self.head
        max_twin_sum = 0

        while first_half and reversed_second:
            twin_sum = first_half.val + reversed_second.val

            max_twin_sum = max(max_twin_sum, twin_sum)

            first_half = first_half.next
            reversed_second = reversed_second.next

        return max_twin_sum

    def Display(self):
        temp = self.head

        while temp is not None:
            print(temp.val, end="")

            if temp.next is not None:
                print(" -> ", end="")

            temp = temp.next

        print()


# -------------------------------
# Create nodes
# -------------------------------

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

# Link nodes
node1.next = node2
node2.next = node3
node3.next = node4

# Create linked list
ll = LinkedList()
ll.head = node1

# Display original linked list
print("Original Linked List:")
ll.Display()

# Find maximum twin sum
result = ll.maximumTwinSum()

print("Maximum Twin Sum:", result)