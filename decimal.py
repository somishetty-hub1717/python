n=101011
n=str(n)
s1=n[::-1]
decimal=0
for i in range(len(s1)):
    decimal+=int(s1[i])*(2**i)
print(decimal)

    
    
    