n = int(input())
count = 0
while 0 < n:
    rem = n % 10
    count += 1
    n //= 10
print(count)
