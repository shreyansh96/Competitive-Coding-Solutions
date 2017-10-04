n=int(input())
array=list(map(int,input().split()))
mean=sum(array)/n
i=0
sumDistSquareMean=0
while i < n:
    sumDistSquareMean+=(array[i]-mean)**2
    i+=1
standardDev=(sumDistSquareMean/n)**0.5
print(round(standardDev,1))
    
    
