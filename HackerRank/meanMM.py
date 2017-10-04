n=int(input())
array =sorted(map(int,input().split()))

print(sum(array)/n)

if n%2==0:
   print ((array[n//2]+array[(n//2)-1])/2)
else:
    print (array[n//2])
print(max(array, key = array.count))
