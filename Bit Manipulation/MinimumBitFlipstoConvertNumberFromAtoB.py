a = 5
b = 9

ans = a ^ b
count = 0
while ans:
    ans = ans & (ans -1)
    count += 1

print(count)