n=int(input())
arr=list(map(int,input().split()))
ans=0
found=False
for i in range(n):
    left=sum(arr[:i])
    right=sum(arr[i+1:])
    if left==right:
        found=True
        ans=i+1
        break
if not found:
    print("NOT FOUND")
else:
    print(ans)

