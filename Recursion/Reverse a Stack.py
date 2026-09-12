def insert(stack, value):
    if not stack:
        stack.append(value)
    else:
        temp = stack.pop()

        insert(stack, value)

        stack.append(temp)


def reverseStack(stack):
    # Base case
    if not stack:
        return

    # Remove top element
    value = stack.pop()

    # Recursively reverse remaining stack
    reverseStack(stack)

    # Insert removed element into correct position
    insert(stack, value)

stack = [4, 1, 3, 2]

print("Original Stack:", stack)
reverseStack(stack)

print("Reversed Stack:", stack)

"""
DRY RUN OF STACK REVERSAL (Input: stack = [4, 1, 3, 2])

* Note: In Python, the top of the stack is the rightmost element.


PHASE 1: UNWINDING (Popping all elements via reverseStack)

1. Call reverseStack([4, 1, 3, 2]) -> Pops value = 2. Remaining stack: [4, 1, 3]
2. Call reverseStack([4, 1, 3])    -> Pops value = 3. Remaining stack: [4, 1]
3. Call reverseStack([4, 1])       -> Pops value = 1. Remaining stack: [4]
4. Call reverseStack([4])          -> Pops value = 4. Remaining stack: []
5. Call reverseStack([])           -> Stack is empty. Base case hit. Returns.


PHASE 2: WINDING (Inserting elements at bottom via insert)

--- 1. Insert value = 4 into stack [] ---
* Stack is empty.
* Condition 'if not stack' matches.
* Action: append(4)
* Current Stack: [4]

--- 2. Insert value = 1 into stack [4] ---
* Stack is not empty.
* Action: pop() -> temp = 4. Stack becomes []
* Recursive Call: insert([], 1) -> Stack is empty -> append(1) -> Stack is [1]
* Restore Action: append(temp)  -> append(4)
* Current Stack: [1, 4]

--- 3. Insert value = 3 into stack [1, 4] ---
* Stack is not empty.
* Action: pop() -> temp1 = 4. Stack becomes [1]
* Recursive Call: insert([1], 3)
  * Stack is not empty.
  * Action: pop() -> temp2 = 1. Stack becomes []
  * Recursive Call: insert([], 3) -> Stack is empty -> append(3) -> Stack is [3]
  * Restore Action: append(temp2) -> append(1) -> Stack becomes [3, 1]
* Restore Action: append(temp1) -> append(4)
* Current Stack: [3, 1, 4]

--- 4. Insert value = 2 into stack [3, 1, 4] ---
* Stack is not empty.
* Action: pop() -> temp1 = 4. Stack becomes [3, 1]
* Recursive Call: insert([3, 1], 2)
  * Stack is not empty.
  * Action: pop() -> temp2 = 1. Stack becomes [3]
  * Recursive Call: insert([3], 2)
    * Stack is not empty.
    * Action: pop() -> temp3 = 3. Stack becomes []
    * Recursive Call: insert([], 2) -> Stack is empty -> append(2) -> Stack is [2]
    * Restore Action: append(temp3) -> append(3) -> Stack becomes [2, 3]
  * Restore Action: append(temp2) -> append(1) -> Stack becomes [2, 3, 1]
* Restore Action: append(temp1) -> append(4)
* Current Stack: [2, 3, 1, 4]

FINAL RESULT: [2, 3, 1, 4]
"""