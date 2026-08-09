def floorSqrt(n: int) -> int:
        if n < 2 :
             return n
        
        low = 1
        high = n // 2
        ans = 1

        while low <= high:
            mid = low + (high-low) // 2

            if mid * mid <= n:
                ans = mid
                low = mid+1
            else:
                high = mid-1

        return ans

n = 63
print(floorSqrt(n))