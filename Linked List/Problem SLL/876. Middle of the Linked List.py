class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def middleNode1(self):
        count = 0
        temp = self.head

        while temp :
            count += 1
            temp = temp.next
            
        temp = self.head
        for _ in range(count // 2):
            temp = temp.next

        self.head = temp

        return self.head

    # TortoiseHare Method
    def middleNode2(self):
        slow = fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        self.head = slow
        return self.head

    # Display Linked List
    def Display(self):
        current = self.head
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None")


# Create nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

# Link nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

head = node1
ll = LinkedList()

ll.head = head

ll.Display()

# ll.middleNode1()
ll.middleNode2()

ll.Display()