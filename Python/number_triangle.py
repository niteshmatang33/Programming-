n=int(input("Enter a number: "))
m=False
for i in range(1,n+1):
    if(m):
        break
    for j in range(n-i):
        print("  ",end="")
    for k in range(i):
        if(i!=n+1):
            print(i,"  ",end="")
            i= i+1
            if(i==n):
                m=True
    print()           