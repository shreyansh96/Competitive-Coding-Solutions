string=str(input())
a=[]
j=0
kevinScore=0
stuartScore=0
while j<len(list(string)):
    i=1
    while j+i <=len(list(string)):
        a.append(string[j:j+i])
        i+=1
        if string[j:j+1] in ('A','E','I','O','U'):
            kevinScore+=1
        else:
            stuartScore+=1
    j+=1
if kevinScore>stuartScore:
    print ('Kevin',kevinScore)
elif kevinScore==stuartScore:
    print ('Draw')
else:
    print ('Stuart',stuartScore)
