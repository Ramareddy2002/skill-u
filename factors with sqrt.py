n=int(input())
import math
for i in range(1,int(n**0.5)+1):
    if(n%i==0):
        print(i,end=" ")
        if(n//i!=i):
            print(n//i,end=' ')
            
   '''
100
1 100 2 50 4 25 5 20 10

125
1 125 5 25
   '''
