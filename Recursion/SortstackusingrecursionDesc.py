class Solution:

    def insert(self, stack, value):
        # If stack is empty or top is <= value,
        # value can be placed directly.
        if not stack or stack[-1] <= value:
            stack.append(value)
        else:
            # Temporarily remove the top element
            temp = stack.pop()

            # Insert value into the correct position
            self.insert(stack, value)

            # Restore the removed element
            stack.append(temp)

    def sortStack(self, stack):
        # Base case
        if not stack:
            return

        # Remove top element
        value = stack.pop()

        # Recursively sort remaining stack
        self.sortStack(stack)

        # Insert removed element into correct position
        self.insert(stack, value)


# -------------------------
# Test
# -------------------------

stack = [4, 1, 3, 2]

solution = Solution()
solution.sortStack(stack)

print("Sorted Stack:", stack)