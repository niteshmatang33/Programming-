n=int(input("Enter a number: "))
x=1
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i):
            print(x," ",end="")
            x=x+1
    print()