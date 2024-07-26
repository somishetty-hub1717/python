s=['aba','sasdad','aaaccc','tapdog','emepe']
count=0
for i in s:
    if i==i[::-1]:
        count+=1
    else:
        mid=len(i)//2
        if len(i)%2==0:
            first_half=i[:mid]
            second_half=i[mid:]
            if first_half==first_half[::-1] or second_half==second_half[::-1]:
                count+=1
        else:
            first_half=i[:mid+1]
            second_half=i[mid:]
            if first_half==first_half[::-1] or second_half==second_half[::-1]:
                count+=1
print(count)
  

   
    

            