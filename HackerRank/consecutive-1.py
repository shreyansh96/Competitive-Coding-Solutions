def consecutive(binaryString):
    listInput=list(str(binaryString))
    ct=[0 for i in range(len(str(binaryString))//2+1)]
    listInput=[int(i) for i in listInput]
    j=0
    for i in range(len(str(binaryString))):
        if listInput[i]== 1:
            ct[j]+=1

        else:
            j+=1
    return (max(ct))
