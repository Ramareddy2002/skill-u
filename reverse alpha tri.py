n=int(input())
for i in range(n,0,-1):
    for j in range(65,65+i):
        a=chr(j)
        print(a,end=' ')
    print()


  '''
5
A B C D E 
A B C D 
A B C 
A B 
A
   '''
