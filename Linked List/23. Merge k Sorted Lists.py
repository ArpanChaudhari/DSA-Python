# Definition for singly-linked list
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Create Linked List from Python List

def createLL(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    temp = head

    for val in arr[1:]:
        temp.next = ListNode(val)
        temp = temp.next

    return head


# Display Linked List
def displayLL(head):
    temp = head

    while temp:
        print(temp.val, end=" -> ")
        temp = temp.next

    print("None")


# Solution

class Solution:

    def mergeLL(self, list1, list2):

        t1 = list1
        t2 = list2

        dummy = ListNode(-1)
        tail = dummy

        while t1 and t2:

            if t1.val < t2.val:
                tail.next = t1
                tail = tail.next
                t1 = t1.next
            else:
                tail.next = t2
                tail = tail.next
                t2 = t2.next

        while t1:
            tail.next = t1
            tail = tail.next
            t1 = t1.next


        while  t2:
            tail.next= t2
            tail = tail.next
            t2 = t2.next

        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        # Solution 1: Merge one by one 
        # TC: O(N*K) where N is the total number of nodes and K is the number of linked lists
        # SC: O(1)
        '''
        result = lists[0]

        for i in range(1,len(lists)):
            result = self.mergeLL(result,lists[i])

        return result
        '''

        # Solution 2: Merge using Divide and Conquer
        # TC: O(N*logK) where N is the total number of nodes and K is the number of linked lists
        # SC: O(k) we create new_lists contains at most k linked-list heads

        while len(lists) > 1:

            new_lists = []

            for i in range(0,len(lists),2):
                if i+1 < len(lists):
                    merged_pair = self.mergeLL(lists[i], lists[i+1])
                    new_lists.append(merged_pair)
                else:
                    new_lists.append(lists[i])
                
            lists = new_lists

        return lists[0]

# MAIN
# Create multiple sorted linked lists

list1 = createLL([1, 4, 5])
list2 = createLL([1, 3, 4])
list3 = createLL([2, 6])


# Display original lists

print("List 1:")
displayLL(list1)

print("List 2:")
displayLL(list2)

print("List 3:")
displayLL(list3)


# Put all lists inside a Python list
lists = [list1, list2, list3]


# Create Solution object
solution = Solution()


# Merge K sorted linked lists
mergedHead = solution.mergeKLists(lists)


# Display result
print("\nMerged Linked List:")
displayLL(mergedHead)