def minFlips(a: int, b: int, c: int) -> int:
    """
    if c_bit == 1, a_bit and b_bin must have and only have one 1;
    if c_bit == 0, a_bit and b_bit must both are 0s.
    """
    ans = 0
    for i in range(32):
        x = (a >> i) & 1
        y = (b >> i) & 1
        z = (c >> i) & 1

        if z == 1:
            ans += (x | y) == 0
        else:
            ans += x + y
    return ans


a = 2
b = 6
c = 5
print(minFlips(a,b,c))