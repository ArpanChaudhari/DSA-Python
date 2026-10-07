class Solution:
    def countMinimumRemovals(self, s: str) -> int:
        open_count = close_count = 0

        for br in s:
            if br == "(":
                open_count += 1
            elif br == ")":
                if open_count > 0:
                    open_count -= 1
                else:
                    close_count += 1

        return open_count + close_count

    def generateValidStrings(
        self,
        index: int,
        balance: int,
        remove_count: int,
        current_string: str,
        s: str,
        minimum_removals: int,
        results: set,
    ):

        # Base case
        if index == len(s):
            if balance == 0 and remove_count == minimum_removals:
                results.add(current_string)
            return

        # Invalid balance: too many ')'
        if balance < 0:
            return

        # Already removed more than necessary
        if remove_count > minimum_removals:
            return

        br = s[index]

        # Case 1: Current character is '('
        if br == "(":

            # Choice 1: Keep '('
            self.generateValidStrings(
                index + 1,
                balance + 1,
                remove_count,
                current_string + "(",
                s,
                minimum_removals,
                results,
            )

            # Choice 2: Remove '('
            self.generateValidStrings(
                index + 1,
                balance,
                remove_count + 1,
                current_string,
                s,
                minimum_removals,
                results,
            )

        # Case 2: Current character is ')'
        elif br == ")":

            # Choice 1: Keep ')'
            self.generateValidStrings(
                index + 1,
                balance - 1,
                remove_count,
                current_string + ")",
                s,
                minimum_removals,
                results,
            )

            # Choice 2: Remove ')'
            self.generateValidStrings(
                index + 1,
                balance,
                remove_count + 1,
                current_string,
                s,
                minimum_removals,
                results,
            )

        # Case 3: Current character is a letter
        else:

            # Letters cannot be removed
            self.generateValidStrings(
                index + 1,
                balance,
                remove_count,
                current_string + br,
                s,
                minimum_removals,
                results,
            )

    def removeInvalidParentheses(self, s: str) -> list[str]:

        # Step 1: Find the minimum number of removals required
        minimum_removals = self.countMinimumRemovals(s)

        # Step 2: Store unique valid answers
        results = set()

        # Step 3: Generate all valid strings using exactly the minimum number of removals
        self.generateValidStrings(0, 0, 0, "", s, minimum_removals, results)

        return list(results)


Solution = Solution()
s = "()())()"
print(Solution.removeInvalidParentheses(s))