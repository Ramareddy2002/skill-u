n=int(input())
f=int(input())
c=0
def fact(n,f,c):
    for i in range(1,n//2+1):
        if n%i==0:
            c+=1
            if c==f:
                return i
    else:
        return 0
        
print(fact(n,f,c))

    '''
60 #n
5 #f
5 #i - 5th factor of 60

24 #n
6 #f
8 #i - 6th factor of 24
    '''
