n=int(input())
for i in range(1,n+1):
    for j in range(65,65+i):
        a=chr(j)
        print(a,end=' ')
    print()

'''
5
A 
A B 
A B C 
A B C D 
A B C D E
'''
