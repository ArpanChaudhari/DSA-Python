class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None

    # Insert At Beginning (O(1))
    def Insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert At End (O(n))
    def insert_at_end(self, data):
        new_node = Node(data) # Initialize node

        if self.head is None: # if ll is empty then insert new node and return
            self.head = new_node
            return
        current = self.head 
        while current.next is not None: # find last node addresh
            current = current.next
        current.next = new_node

    # Insert at Specific Value (O(n))
    def insert_at_target(self,target,data):
        current = self.head
        while current and current.data != target: # find target Node
            current = current.next

        if current is None: # if target not in LL
            print(f"Target({target}) node not found")
            return

        new_node = Node(data) # Initilize node
        new_node.next = current.next # connect new_node node with  target next
        current.next = new_node # now , connect target with new_node

    # Display Linked List
    def Display(self):
        current = self.head

        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None")

ll = Linked_list()

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

ll.Insert_at_beginning(8)
ll.Insert_at_beginning(6)

ll.Display()

ll.insert_at_end(18)

ll.Display()

ll.insert_at_target(10,11) # coonect 
ll.insert_at_target(20,22) # not found  

ll.Display() # then display