armstrong_list = []
for n in range(1,1001):
    length = len(str(n))
    temp2 = n
    res = 0
    while 0 < temp2:
        rem = temp2 % 10
        res = res + res ** length
        temp2 //= 10

    if res == n:
        armstrong_list.append(n)
print(armstrong_list)
