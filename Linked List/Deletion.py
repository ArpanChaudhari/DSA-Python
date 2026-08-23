class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList :
    def __init_(self):
        self.head = None

    # Deletion at Beginning
    def deletion_at_beginning(self):

        if self.head is None:
            return

        # move head to next
        self.head = self.head.next

    # Deletion at End
    def deletion_at_End(self):

        if self.head is None:
            return

        # If Only One node
        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next.next is not None: # Find second last node
            current = current.next

        current.next = None

    # Deletion at target
    def deletion_at_target(self,target):
        if self.head is None:
            return

        # Target is the first node
        if self.head.data == target:
            self.head = self.head.next
            return
        
        current = self.head
        while current and current.next.data != target:
            current = current.next

        current.next = current.next.next

    # Display Linked List
    def Display(self):
        current = self.head
    
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None")

ll = LinkedList()

# Create given  nodes
node1 = Node(10)
node2 = Node(12)
node3 = Node(14)
node4 = Node(16)

# Link nodes
node1.next = node2
node2.next = node3
node3.next = node4

ll.head = node1

ll.Display()

# ll.deletion_at_beginning()
# print("Deletion At Beginning:")
# ll.Display()

# ll.deletion_at_End()
# print("Deletion At End")
# ll.Display()

ll.deletion_at_target(10)
ll.Display()