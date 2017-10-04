##Quartile: Any of three points that divide an ordered distribution into
##          four parts each containing one quarter of the soores.
def median(n,array):
    if n%2==0:
        return (array[n//2]+array[n//2-1])/2
    else:
        return array[n//2]
    
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
        Q3=median(len(array2),array2)    
    print(int(Q1),int(Q2),int(Q3))


n=int(input())
array=sorted(map(int,input().split()))
quartile(n,array)
