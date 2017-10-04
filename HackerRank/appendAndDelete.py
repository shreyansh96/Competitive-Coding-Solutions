operations=int(input())
string1=str(input())
string2=str(input())
commonLength=0
i=0
strLen1=len(string1)
strLen2=len(string2)
while i<min(strLen1,strLen2):
    if string1[i]==string2[i]:
        commonLength+=1
        i+=1
    else:
        break
if ((strLen1+strLen2)-(2*commonLength))>operations:
    print('No')
elif ((strLen1+strLen2)-(2*commonLength))%2==operations%2:
    print('Yes')
elif (strLen1+strLen2)<operations:
    print('Yes')
else:
    print('No')


##list1=list(string1)
##list2=list(string2)
##i=0
##if len(list1)>len(list2):
##    while i < len(list2):
##        if list2[i] in list1:
##            list1.remove(list2[i])
##            list2.remove(list2[i])
##            i=i-1
##            print(list1,list2)
##        i+=1
##else:
##    while i < len(list1):
##        if list1[i] in list2:
##            list2.remove(list1[i])
##            list1.remove(list1[i])
##            i=i-1
##            print(list1,list2)
##        i+=1
##length=len(list1)+len(list2)
##if length<=operations:
##    print('Yes')
##else:
##    print('No')
