n=int(input("Enter a number: "))
m=n
for i in range(0,n):
    for j in range(i):
        print(" ",end="")
    for k in range(m):
        print("+ ",end="")
        
    m=m-1    
    print()    