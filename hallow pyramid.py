#hallow pyramid
x=int(input())
for i in range(x):
    for j in range(x-i-1):
        print(" ",end=" ")
    for j in range(2*i+1):
        if j==0 or i==x-1 or j==2*i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()