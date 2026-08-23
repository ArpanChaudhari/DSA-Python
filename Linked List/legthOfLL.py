class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def length(self):
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next

        return count

    def display(self):
        current = self.head

        while current:
            print(current.data, end=" → ")
            current = current.next

        print("None")


ll = LinkedList()

ll.head = Node(10)
ll.head.next = Node(20)
ll.head.next.next = Node(30)
ll.head.next.next.next = Node(40)

ll.display()

print("Length:", ll.length())