def scoreOfParentheses(s: str) -> int:
    n = len(s)
    stack = [0]  # first item in stack for final result

    for br in s:

        if br == "(":
            stack.append(0)
        else:
            inside_score = stack.pop()

            if inside_score == 0:
                current_score = 1
            else:
                current_score = 2 * inside_score

            stack[-1] += current_score

    return stack[0]

s = "(()(()))"
print(scoreOfParentheses(s))  # Output: 6

"""
stack = [0]
i = 0 -> "(" -> stack = [0, 0]
i = 1 -> "(" -> stack = [0, 0, 0]
i = 2 -> ")" -> inside_score = 0 -> current_score = 1 -> stack[-1] += 1 -> stack = [0, 1]
i = 3 -> "(" -> stack = [0, 1, 0]
i = 4 -> "(" -> stack = [0, 1, 0, 0]
i = 5 -> ")" -> inside_score = 0 -> current_score = 1 -> stack[-1] += 1 -> stack = [0, 1, 1]
i = 6 -> ")" -> inside_score = 1 -> current_score = 2 * 1 = 2 -> stack[-1] += 2 -> stack = [0, 3]
i = 7 -> ")" -> inside_score = 3 -> current_score = 2 * 3 = 6 -> stack[-1] += 6 -> stack = [6]
return stack[0] = 6
"""