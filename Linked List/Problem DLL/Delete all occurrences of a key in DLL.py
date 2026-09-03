class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


def deleteAllOccurrences(head, target):

    # Remove target nodes from the beginning
    while head and head.data == target:
        head = head.next

    # Fix prev pointer of new head
    if head:
        head.prev = None

    temp = head

    # Delete remaining target nodes
    while temp:
        if temp.data == target:

            if temp.prev:
                temp.prev.next = temp.next

            if temp.next:
                temp.next.prev = temp.prev

        temp = temp.next

    return head


# Create Doubly Linked List
def createDLL(values):
    if not values:
        return None

    head = Node(values[0])
    temp = head

    for value in values[1:]:
        new_node = Node(value)

        temp.next = new_node
        new_node.prev = temp

        temp = new_node

    return head


# Display Doubly Linked List
def displayDLL(head):
    temp = head

    while temp:
        print(temp.data, end="")

        if temp.next:
            print(" <-> ", end="")

        temp = temp.next

    print()


# Test
head = createDLL([2, 1, 2, 3, 2, 4])

print("Original Doubly Linked List:")
displayDLL(head)


target = 2
head = deleteAllOccurrences(head, target)


print("After Deleting Target:")
displayDLL(head)