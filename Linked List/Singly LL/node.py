class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


# Create nodes
node1 = Node(10)
node2 = Node(12)
node3 = Node(14)
node4 = Node(16)

# Link nodes
node1.next = node2
node2.next = node3
node3.next = node4

head = node1

# Traverse and print the Linked list

# Approach 1
current = head

while current:
    print(current.data,end=" -> ")
    current = current.next
print("None")

# Approach 2
def traverseList(head):

    if head is None:
        return

    print(head.data,end="")

    if head.next is not None:
        print(" -> ", end="")

    traverseList(head.next)

traverseList(head)