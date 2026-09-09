class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createLL(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    temp = head

    for val in arr[1:]:
        temp.next = ListNode(val)
        temp = temp.next

    return head


def displayLL(head):
    temp = head

    while temp:
        print(temp.val, end=" -> ")
        temp = temp.next

    print("None")


class Solution:
    def swapPairs(self, head):
        if head is None:
            return None

        # make dummy node
        dummy = ListNode(-1)

        # connect with head
        dummy.next = head

        prev = dummy

        # need next element is not None and also pair
        while prev.next and prev.next.next:
            # prev → first → second → next
            first = prev.next
            second = first.next

            # prev → second → first → next
            prev.next = second
            first.next = second.next
            second.next = first

            # move prev to first for next pair
            prev = first

        return dummy.next


arr = [1, 2, 3, 4, 5]

head = createLL(arr)

print("Original Linked List:")
displayLL(head)

solution = Solution()
head = solution.swapPairs(head)

print("\nAfter Swapping Pairs:")
displayLL(head)