class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


def reverseLL(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

# Iterative approach
def addOne(head):
    head = reverseLL(head)

    carry = 1
    temp = head

    while temp:
        node_sum = temp.data + carry
        temp.data = node_sum % 10
        carry = node_sum // 10

        if temp.next is None and carry:
            temp.next = Node(carry)
            carry = 0

        temp = temp.next

    return reverseLL(head)

# Recursive approach
def addOneUtils(node):
    if node is None:
        return 1

    carry = addOneUtils(node.next)
    node_sum = node.data + carry
    node.data = node_sum % 10
    carry = node_sum // 10

    return carry
def recursiveAddOne(head):

    carry = addOneUtils(head)

    if carry:
        new_head = Node(carry)
        new_head.next = head
        head = new_head
    return head


# Create Linked List
def createLinkedList(values):
    if not values:
        return None

    head = Node(values[0])
    temp = head

    for value in values[1:]:
        temp.next = Node(value)
        temp = temp.next

    return head


# Display Linked List
def displayLinkedList(head):
    temp = head

    while temp:
        print(temp.data, end="")
        if temp.next:
            print(" -> ", end="")
        temp = temp.next

    print()


# Test
head = createLinkedList([9, 9, 9])

print("Original Linked List:")
displayLinkedList(head)

# head = addOne(head)
head = recursiveAddOne(head)

print("After Adding One:")
displayLinkedList(head)