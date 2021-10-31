x=[1,-3,-4,4,2,-6,-2,-8,10]
neg= lambda x: True if x<0 else False

soham=filter(neg,x)
for j in soham:
    print(j)
