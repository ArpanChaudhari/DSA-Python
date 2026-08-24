class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Deletion at Beginning
    def deletion_at_beginning(self):
        if self.head is None:
            return
         
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None 

    # Deletion at End
    def deletion_at_end(self):
        if self.head is None:
            return

        # Only one node
        if self.head.next is None:
            self.head = None
            return
        
        temp = self.head
        while temp and temp.next.next is not None:
            temp = temp.next

        temp.next = None

    # Deletion at Target
    def deletion_at_target(self,target):
        if self.head is None:
            return

        # Target is the first node
        if self.head.data == target:
            self.head = self.head.next

            if self.head is not None:
                self.head.prev = None
                return

        temp = self.head
        while temp and temp.data != target:
            temp = temp.next

        if temp is None:
            print(f"Target{target} node is not found.")

        temp.prev.next  = temp.next

        # If target is not the last node
        if temp.next is not None:
            temp.next.prev = temp.prev
        

    def Display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end="")
            if temp.next is not None:
                print(" <-> ", end="")
            temp = temp.next
        print()

ll = LinkedList()

node1 = Node(1)
head = node1
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node2.prev = node1
node3.prev = node2
node4.prev = node3
node5.prev = node4

ll.head = node1

ll.Display()

# ll.deletion_at_beginning()

# ll.Display()

# ll.deletion_at_end()

# ll.Display()

ll.deletion_at_target(4)

ll.Display()
