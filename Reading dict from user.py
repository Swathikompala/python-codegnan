n = int(input())
d = {}
for i in range(0,n,1):
    key, value = map(int, input().split())
    d[key] = value
print(d)
