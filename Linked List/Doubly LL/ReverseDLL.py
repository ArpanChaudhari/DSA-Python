class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def reverseList_by_using_spaace(self): # Time-Complexity:- O(n)  & Space Complexity:- O(n)
        head = self.head

        if head is None or head.next is None:
            return head

        stack = []

        temp = head
        while temp and temp is not None:
            stack.append(temp.val)
            temp = temp.next

        temp = head
        while temp:
            temp.val = stack.pop()
            temp = temp.next

        return head

    def reverseList_in_place(self): # Time-Complexity:- O(n)  & Space Complexity:- O(1)
        new_head = None
        current = self.head

        while current is not None:
            # Current node will become the new head
            new_head = current

            # Swap prev and next
            current.prev, current.next = current.next, current.prev

            # Move to the next node
            current = current.prev

        self.head = new_head
        return self.head
            
    
    def Display(self):
        temp = self.head
        while temp is not None:
            print(temp.val, end="")
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

# ll.reverseList_by_using_spaace()
ll.reverseList_in_place()

ll.Display()
