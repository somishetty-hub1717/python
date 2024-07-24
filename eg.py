arr=[1,1,0,1,1,0,0]
l1=[]
l2=[]
for i in range(len(arr)):
    if arr[i]==0:
        l1.append(0)
    if arr[i]==1:
        l2.append(1)
print(l1+l2)