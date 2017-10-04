def num2bin(number):
    import math
    i=0
    rem=[0 for i in range(1+int(math.log(number,2)))]
    while number!=1:
        rem[i]=number%2
        number=number//2
        i+=1
    rem[i]=1
    binaryList=rem[::-1]
    return "".join([(str(e)) for e in binaryList])
    
