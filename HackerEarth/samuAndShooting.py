t=int(input())
for i in range(t):
    X,Y,N,W,P1,P2=map(int,input().split())
    if Y*N<W & X*N<W:
        print(0)
    elif P1>P2:
        if X*N>=W:
            for i in range (N):
                if X*i>=W:
                    print('%0.6f'% ((P1/100)**i))
        else:
            
            for i in range(N):
                if X*(N-i)+Y*i>=W:
                     prob=((P1/100)**(N-i))*((P2/100)**i)
                     print( '%0.6f'%(prob*100))    
    elif P2>P1:
        if Y*N>=W:
            for i in range (N):
                if Y*i>=W:
                    print('%0.6f'% ((P2/100)**i))
        else:
            
            for i in range(N):
                if Y*(N-i)+X*i>=W:
                     prob=((P1/100)**(N-i))*((P2/100)**i)
                     print( '%0.6f'%(prob*100))    
        
