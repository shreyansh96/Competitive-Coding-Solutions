##Quartile: Any of three points that divide an ordered distribution into
##          four parts each containing one quarter of the soores.
def median(n,array):
    if n%2==0:
        return float((array[n//2]+array[n//2-1])/2)
    else:
        return float(array[n//2])
    
def quartile(n,array):
    if n%2==0:
        Q2=median(n,array)
        array1=array[0:n//2]
        array2=array[n//2:n]
        Q1=median(len(array1),array1)
        Q3=median(len(array2),array2)
        
    else:
        Q2=median(n,array)
        array1=array[0:n//2]
        array2=array[n//2+1:n]
        Q1=median(len(array1),array1)
        print (Q1)
        print(Q2)
        Q3=median(len(array2),array2)    
        print (Q3)
    return Q1, Q2,Q3

n=int(input())
array=list(map(int,input().split()))
frequencies=list(map(int,input().split()))
i=0
c=[]

while i<n:
    j=0
    while j<frequencies[i]:
        c.append(array[i])
        j+=1
    i+=1
Q1,Q2,Q3=quartile(len(c),sorted(c))
print(round(Q3-Q1,1))

