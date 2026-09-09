class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


def createLL(values, random_indices):
    if not values:
        return None

    nodes = []

    for val in values:
        nodes.append(Node(val))

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    for i in range(len(nodes)):
        if random_indices[i] is not None:
            nodes[i].random = nodes[random_indices[i]]

    return nodes[0]


def displayLL(head):
    temp = head

    print("Next:   ", end="")
    while temp:
        print(temp.val, end=" -> ")
        temp = temp.next
    print("None")
    temp = head

    print("Random: ", end="")
    while temp:
        if temp.random:
            print(temp.random.val, end=" -> ")
        else:
            print("None", end=" -> ")
        temp = temp.next
    print("None")


class Solution:
    def insertCopyInBetween(self, head):
        temp = head
        while temp:
            copyNode = Node(temp.val) # Create copy Node

            nextNode = temp.next # preserve next node

            temp.next = copyNode # connect temp with copyNode 
            
            copyNode.next = nextNode # connect copynode with nextNode
            
            temp = nextNode  # Move temp to main next node
    
    def connectRandomPointers(self, head):
        temp = head
        while temp:
            copyNode = temp.next # select copyNode
            if temp.random: 
                copyNode.random = temp.random.next # connect random pointer for copyNodes
            else:
                copyNode.random = None

            temp = temp.next.next

    def getDeepCopyList(self, head):
        temp = head
        dummy = Node(-1)
        curr = dummy

        while temp:
            curr.next = temp.next # select copyNode
            curr = curr.next # move copyNode to next 

            temp.next = temp.next.next # connect temp with main next node
            temp = temp.next # Move temp to next
        
        return dummy.next
    
    def copyRandomList(self, head):
        if head is None:
            return None

        # Solution 1 --> TC - O(n) and SC - O(n)
        '''
        hashmap = {}

        temp = head

        while temp:
            hashmap[temp] = Node(temp.val)
            temp = temp.next

        temp = head

        while temp:
            hashmap[temp].next = hashmap.get(temp.next)
            hashmap[temp].random = hashmap.get(temp.random)

            temp = temp.next

        return hashmap[head]
        '''

        # Solution 2 --> TC - O(n) and SC - O(1)
        # insertCopyInBetween
        self.insertCopyInBetween(head) # -> O(n) 

        # connectRandomPointers
        self.connectRandomPointers(head) # -> O(n)

        # getDeepCopyList
        return self.getDeepCopyList(head) # -> O(n)


values = [7, 13, 11, 10, 1]

random_indices = [None, 0, 4, 2, 0]

head = createLL(values, random_indices)

print("Original Linked List:")
displayLL(head)

solution = Solution()
copied_head = solution.copyRandomList(head)

print("\nCopied Linked List:")
displayLL(copied_head)