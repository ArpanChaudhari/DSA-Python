class Solution:
    # Time: O(3^k) worst case & Space: O(n) recursion stack
    """
    def solve(self, s, index, balance):
        if balance < 0:
            return False

        if index == len(s):
            return balance == 0

        if s[index] == "(":
            return self.solve(s, index + 1, balance + 1)
        elif s[index] == ")":
            return self.solve(s, index + 1, balance - 1)
        else:
            return (
                self.solve(s, index + 1, balance)
                or self.solve(s, index + 1, balance + 1)
                or self.solve(s, index + 1, balance - 1)
            )
        """

    def checkValidString(self, s: str) -> bool:
        # Approach 1 
        # return self.solve(s, 0, 0)

        # Approach 2
        # 'low' = minimum possible number of unmatched '('
        # 'high' = maximum possible number of unmatched '('
        low = high = 0

        for br in s:

            # '(' increase the number of open brackets
            if br == "(":
                low += 1
                high += 1

            # ')' close an open bracket    
            elif br == "*":
                low -= 1
                high += 1
            
            # '*' can become:
            # 1. ')'  -> minimum balance decreases
            # 2. '('  -> maximum balance increases
            # 3. "" -> range[low, high]
            else:
                low -= 1
                high -= 1
            
            # A negative balance is not possible.
            low = max(0, low)

            if high < 0:
                return False
                
        # low == 0 means balance 0 is possible.
        return low == 0

    


# s = "())*("
s = "(*))"
Solution = Solution()
print(Solution.checkValidString(s))
