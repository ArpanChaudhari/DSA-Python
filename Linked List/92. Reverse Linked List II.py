class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head, left, right):
        if left == right:
            return head

        left_prev = None
        temp1 = head

        for _ in range(left - 1):
            left_prev = temp1
            temp1 = temp1.next

        temp2 = head
        for _ in range(right - 1):
            temp2 = temp2.next

        right_next = temp2.next

        prev = right_next
        current = temp1

        while current is not right_next:
            new_node = current.next
            current.next = prev
            prev = current
            current = new_node

        if left_prev:
            left_prev.next = prev
        else:
            head = prev

        return head


# Convert a list into a linked list
def create_linked_list(arr):
    dummy = ListNode()
    current = dummy

    for value in arr:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


# Print the linked list
def print_linked_list(head):
    values = []

    while head:
        values.append(str(head.val))
        head = head.next

    print(" -> ".join(values))


# Take input from the user
ll = [1,2,3,4,5]
left = 1
right = 4

head = create_linked_list(ll)
print_linked_list(head)

solution = Solution()
result = solution.reverseBetween(head, left, right)

print("Reversed linked list:")
print_linked_list(result)