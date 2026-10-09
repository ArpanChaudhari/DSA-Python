def minInsertions(s: str) -> int:
    close_needed = 0
    ans = 0

    for ch in s:
        #
        if ch == "(":

            # If close_needed is odd, one ')' is needed to complete the previous pair.
            if close_needed % 2 != 0:
                ans += 1
                close_needed -= 1

            # The new '(' requires two closing parentheses.
            close_needed += 2

        else:

            # We have a ')' but no '(' is waiting for it.
            if close_needed == 0:
                ans += 1
                # Insert a '(', which requires two ')' characters.
                close_needed += 2

            close_needed -= 1

    # Insert all closing parentheses still required.
    return ans + close_needed


s = "))())("
print(minInsertions(s))