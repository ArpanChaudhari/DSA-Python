class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def search(self, target):

        current = self.head

        while current:

            if current.data == target:
                return True

            current = current.next

        return False


# Create linked list
ll = LinkedList()

ll.head = Node(10)
ll.head.next = Node(20)
ll.head.next.next = Node(30)
ll.head.next.next.next = Node(40)


print(ll.search(30))
print(ll.search(50))