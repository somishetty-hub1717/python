n=int(input())
arr=list(map(int,input().split(" ")))
count=0
total=0
for i in arr:
    total+=i
    if total==0:
        count+=1
print(count)
