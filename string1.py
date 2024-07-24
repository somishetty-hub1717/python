s='abcdz'
s1=''
for i in s:
    if ord(i)>=97 and ord(i)<122:
        s1+=chr(ord(i)+1)
    else:
        s1+=chr(ord(i)-25)
print(s1)


    