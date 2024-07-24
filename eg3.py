arr=[1,2,3,4,5,6]
k=6
count=0
for i in range(0,len(arr)):
    for j in range(0,len(arr)):
        if arr[i]+arr[j]==k:
            count+=1
print(count)