class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node


class Solution:
    def detectCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
        
                return slow.data

        return None


ll = LinkedList()

for value in [3, 2, 0, -4]:
    ll.insert(value)

# Create cycle: last node → node with value 2
ll.head.next.next.next.next = ll.head.next

# Solve
solution = Solution()
print("tail connects to node:",solution.detectCycle(ll.head))