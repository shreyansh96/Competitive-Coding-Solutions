n=int(input())
numberArray =list(map(int,input().split()))
weightArray=list(map(int,input().split()))
i=0
product=0
while i<n:
   product=numberArray[i]*weightArray[i]+product
   i+=1
print (round(product/sum(weightArray),1))

