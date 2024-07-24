arr=[1,2,3,4,5]
k=6
count=0
f=0
l=len(arr)-1
while f<1:
    if arr[f]+arr[l]==k:
        count+=1
    f+=1
    l-=1
print(count)