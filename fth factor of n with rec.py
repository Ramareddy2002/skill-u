n=int(input())
f=int(input())
c=0
i=1
def fact(n,f,c,i):
    if i>n:
        return 0
    if n%i==0:
        c+=1
        if c==f:
            return i
        else:
            return fact(n,f,c,i+1)
    else:
        return (fact(n,f,c,i+1))
print(fact(n,f,c,i))

    
'''    
60
5
5

24
6
8
'''
