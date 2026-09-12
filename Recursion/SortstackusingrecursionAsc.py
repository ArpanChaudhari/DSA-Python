
class Solution:
    def insert(self,stack,value):
        if not stack or stack[-1] >= value:
            stack.append(value)
        else:
            temp = stack.pop()
            self.insert(stack, value)
            stack.append(temp)
            
    def sortStack(self, stack):
        if not stack:
            return

        value = stack.pop()
        self.sortStack(stack)

        self.insert(stack,value)
        


stack = [4, 1, 3, 2]

solution = Solution()
solution.sortStack(stack)

print("Sorted Stack:", stack)