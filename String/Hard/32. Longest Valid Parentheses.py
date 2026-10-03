def longestValidParentheses(s: str) -> int:

    # Opproach 1 --> O(n) time and O(n) space
    """
    stack = []
    boundary = -1
    max_length = 0

    for i in range(len(s)):
        if s[i] == "(":
            stack.append(i)

        else:
            if stack:
                stack.pop()

                if stack:
                    max_length = max(max_length, i - stack[-1])
                else:
                    max_length = max(max_length, i - boundary)

            else:
                boundary = i

    return max_length
    """

    # Approach 2 --> O(n) time and O(1) space
    open_br = 0
    close_br = 0
    max_length = 0

    for i in range(len(s)):
        if s[i] == "(":
            open_br += 1

        else:
            close_br += 1
            
        if open_br == close_br:
            max_length = max(max_length, open_br + close_br)
        elif close_br > open_br:
            open_br = 0
            close_br = 0

    open_br = 0
    close_br = 0
        
    for i in range(len(s)-1,-1,-1):
        if s[i] == ")":
            close_br += 1

        else:
            open_br += 1
            
        if open_br == close_br:
            max_length = max(max_length, open_br + close_br)
        elif open_br > close_br:
            open_br = 0
            close_br = 0

    return max_length



s = ")()())"
print(longestValidParentheses(s))  # Output: 4