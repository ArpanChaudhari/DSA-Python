class Solution:
    def paint(self, A: int, B: int, C: list[int]) -> int:
        MOD = 10000003
        if len(C) <= A:
            return (max(C) * B) % MOD

        low = max(C)
        high = sum(C)

        while low <= high:
            mid = low + (high - low) // 2

            painters = self.countPainters(C,mid)

            if painters <= A:
                high = mid - 1
            else:
                low = mid + 1

        return (low * B) % MOD

    def countPainters(self,C,max_length):
        painters = 1
        current = 0

        for board in C:
            if current + board <= max_length:
                current += board
            else:
                painters += 1
                current = board

        return painters


Sol = Solution() 

A = 4
B = 3
C = [10,20]
print(Sol.paint(A,B,C))