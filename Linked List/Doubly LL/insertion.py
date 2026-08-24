class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insertion at Beginning
    def insertion_at_beginning(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    # Insertion at End
    def insertion_at_end(self,data):
        new_node = Node(data) 

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp and temp.next != None:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    # Insertion at Target
    def insertion_at_target(self,target,data):
        temp = self.head
        while temp and temp.data != target:
            temp = temp.next

        if temp is None:
            print(f"Target{target} node Not Found")
            return

        new_node = Node(data)

        new_node.next = temp.next # connect new node next and prev
        new_node.prev = temp 

        if temp.next is not None: # if target is not last node
            temp.next.prev = new_node

        temp.next = new_node

    # Display Linked List
    def Display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end="")
            if temp.next is not None:
               print(" <-> ", end="")
            temp = temp.next
        print()

# creat node 
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

# Link forward node
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Link backward node
node2.prev = node1
node3.prev = node2
node4.prev = node3
node5.prev = node4

ll = LinkedList()

ll.head = node1

ll.Display()

ll.insertion_at_beginning(0)

ll.Display()

ll.insertion_at_end(7)

ll.Display()

ll.insertion_at_target(5,6)

ll.Display()