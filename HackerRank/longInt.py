
n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
sumPrimary=0
sumSecondary=0
for i in range(n):
    sumPrimary=a[i][i]+sumPrimary
    sumSecondary=a[i][n-i-1]+sumSecondary
    i+=1

print(abs(sumPrimary-sumSecondary))
