class Solution:
    def helper(self, s: str, i: int, num: int, sign: int):

        INT_MIN = -(2**31)
        INT_MAX = 2**31 - 1

        # Base case: end of string or non-digit
        if i >= len(s) or not s[i].isdigit():
            return sign * num

        # Update num
        num = num * 10 + int(s[i])

        # if overflow
        if sign * num <= INT_MIN:
            return INT_MIN
        if sign * num >= INT_MAX:
            return INT_MAX

        return self.helper(s, i + 1, num, sign)

    def myAtoi(self, s: str) -> int:
        sign = 1
        i = 0

        # Skip whitespaces
        while i < len(s) and s[i] == " ":
            i += 1

        # Handle sign
        if i < len(s) and (s[i] == "-" or s[i] == "+"):
            sign = -1 if s[i] == "-" else 1
            i += 1

        return self.helper(s, i, 0, sign)


sol = Solution()
s = "1337c0d3"
print(sol.myAtoi(s))