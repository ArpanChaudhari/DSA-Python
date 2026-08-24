class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

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

temp = head
while temp is not None:
    print(temp.data, end="")
    if temp.next is not None:
        print("<->", end="")
    temp = temp.next
