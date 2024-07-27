alice=input()
bob=input()
a,b=0,0
for i in range(0,len(alice)):
    if alice[i]>bob[i]:
        a+=1
    elif alice[i]<bob[i]:
        b+=1
    else:
        pass      
print(a,b)

        