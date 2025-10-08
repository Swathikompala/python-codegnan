n = int(input())
if n%2==0 and n>0:
    print(f"The number is positive even")
elif n%2==1 and n>0:
    print(f"The number is positive odd")
elif n%2==0 and n<0:
    print(f"The number is Negetive even")
elif  n%2==1 and n<0:
    print(f"The number is Negetive odd")
else:
    print(f"The number is Zero")
