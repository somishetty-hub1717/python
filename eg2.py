s=[4,5,3,1,2]
first=0
last=len(s)-1
while first<last:
    first=s[last]
    last=s[first]
    first+=1
    last-=1
print()

