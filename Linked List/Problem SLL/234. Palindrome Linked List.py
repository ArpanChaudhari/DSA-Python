# Node class represents a node in a linked list
class Node:
    def __init__(self, val, next_node=None):
        self.val = val       # Data stored in the node
        self.next = next_node  # Pointer to the next node in the list

# Function to reverse a linked list using the recursive approach
def reverse_linked_list(head):
    prev = None
    current = head

    while current is not None:
        # Current node will become the new head
        new_node = current.next

        # Swap prev and next
        current.next, prev = prev, current

        # Move to the next node
        current = new_node

    return prev

# Function to check if the linked list is a palindrome
def is_palindrome(head):
    if head is None or head.next is None:
        return True  # It's a palindrome by definition

    slow = head
    fast = head

    # Traverse the linked list to find the middle using slow and fast pointers
    while fast and fast.next:
        slow = slow.next      
        fast = fast.next.next 

    # Reverse the second half of the linked list starting from the middle
    second_half = reverse_linked_list(slow)
    first_half = head

    while first_half and second_half:
        if first_half.val != second_half.val:
            return False
            
        first_half = first_half.next
        second_half = second_half.next
        
    return True

# Function to print the linked list
def print_linked_list(head):
    temp = head
    while temp:
        print(temp.val, end=" ")  # Print the current node's data
        temp = temp.next           # Move to the next node
    print()

# Driver code
if __name__ == "__main__":
    # Create a linked list with values 1, 5, 2, 5, and 1 (15251, a palindrome)
    head = Node(1)
    head.next = Node(5)
    head.next.next = Node(2)
    head.next.next.next = Node(5)
    head.next.next.next.next = Node(1)

    # Print the original linked list
    print("Original Linked List: ", end="")
    print_linked_list(head)

    # Check if the linked list is a palindrome
    if is_palindrome(head):
        print("The linked list is a palindrome.")
    else:
        print("The linked list is not a palindrome.")
