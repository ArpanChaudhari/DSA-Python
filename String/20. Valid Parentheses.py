def isValid(s: str) -> bool:
    # Opproach 1
    """
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        else:
            if not stack:
                return False

            if stack[-1] != pairs[ch]:
                return False

            stack.pop()

    return len(stack) == 0
    """

    # Opproach 2
    stack = []
    for ch in s:
        if ch == "(":
            stack.append(")")
        elif ch == "[":
            stack.append("]")
        elif ch == "{":
            stack.append("}")
        else:
            if not stack or stack[-1] != ch:
                return False
            stack.pop()

    return not stack


# s = "()[]{}"
s= "{[}]"
print(isValid(s))
