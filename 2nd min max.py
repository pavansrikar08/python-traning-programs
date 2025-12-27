x=[2,5,7,1,9]
x1=min(x)
x2=max(x)
min2=float('inf')
max2=float("-inf")
for i in range(len(x)):
    if x1<x[i]<min2:
        min2=x[1]
    if x2>x[i]>max2:
        min2=x[1]
print(min2,max2)