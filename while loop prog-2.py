lst = [1,2,2,3,2,1]
ele = 2
n = len(lst)
i = 0
while i < n:
    if lst[i] == ele:
        lst.pop(i)
        n -= 1
    else:
        i += 1
    
print(lst)
