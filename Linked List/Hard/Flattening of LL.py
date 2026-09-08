
class ListNode:
    def __init__(self, val=0, next=None, child=None):
        self.val = val
        self.next = next
        self.child = child


# Create a Linked List from a list
def createLL(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    temp = head

    for val in arr[1:]:
        temp.child = ListNode(val)
        temp = temp.child

    return head


# Display a Linked List
def displayLL(head):
    temp = head
    result = []

    while temp:
        result.append(str(temp.val))
        temp = temp.child

    print(" -> ".join(result))


# Solution
class Solution:

    def mergeLL(self, list1, list2):

        t1 = list1
        t2 = list2

        dummy = ListNode(-1)
        tail = dummy

        while t1 and t2:

            if t1.val < t2.val:
                tail.child = t1
                tail = t1
                t1 = t1.child

            else:
                tail.child = t2
                tail = t2
                t2 = t2.child

            tail.next = None

        if t1:
            tail.child = t1

        elif t2:
            tail.child = t2

        if dummy.child:
            dummy.child.next = None

        return dummy.child


    def flattenLinkedList(self, head):

        if head is None or head.next is None:
            return head

        # Flatten the remaining lists
        mergeHead = self.flattenLinkedList(head.next)

        # Merge current list with flattened list
        head = self.mergeLL(head, mergeHead)

        return head



# Create individual sorted child lists
list1 = createLL([1, 2, 3])
list2 = createLL([4, 5, 6])
list3 = createLL([7, 8, 9])
list4 = createLL([12, 20])

# Connect them using NEXT pointers
list1.next = list2
list2.next = list3
list3.next = list4


# Display original multilevel linked list
print("Original Linked List:")

temp = list1

while temp:
    print(f"{temp.val} -> ", end="")

    child_temp = temp.child

    while child_temp:
        print(f"{child_temp.val} -> ", end="")
        child_temp = child_temp.child

    print("None")

    temp = temp.next


# Flatten
solution = Solution()
flattenedHead = solution.flattenLinkedList(list1)


# Display flattened linked list
print("\nFlattened Linked List:")
displayLL(flattenedHead)

'''
1 ──next──> 4 ──next──> 7 ──next──> 9 ──next──> 20 ──next──> None
↓           ↓           ↓           ↓
2           5           8           12
↓           ↓           
3           6           


    1 -> 4 -> 7 -> 9 -> 20 -> None so, 
    mergedHead = 20, merge 20,9 -> (9,12,20) -> 9.next == None

    mergesHead = 9 , merge 7,9 -> (7,8,9,12,20) -> 7.next == None

    mergedHead = 7 , merge 4,7 -> (4,5,6,7,8,9,12,20) -> 4.next == None
    
    mergedHead == 4 , merge 1,4 -> (1,2,3,4,5,6,7,8,9,12,20) -> 1.next == None
    
    return 1
'''