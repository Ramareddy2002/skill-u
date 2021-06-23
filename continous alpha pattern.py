n=int(input())
c=65
for i in range(65,65+n):
    for j in range(65,i+1):
        a=chr(c)
        print(a,end=' ')
        c+=1
    print()

'''
5
A 
B C 
D E F 
G H I J 
K L M N O
'''
