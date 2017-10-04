n,k=map(int,input().split())
Set=list(map(int,imput().split())
subset=[]         
for i in Set:
    for j in Set:
        if i==j:
            continue
        elif (i+j)%k==0:
            subset.append(j)
        
         
