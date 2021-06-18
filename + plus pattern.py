n=int(input('Enter  num: '))
if n%2!=0:
    for i in range (1,n+1):
        for j in range (1,n+1):
            if (i==n//2+1 or j==n//2+1):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
else:
    print('Entered wrong input')

    '''
Enter  num: 7
      *       
      *       
      *       
* * * * * * * 
      *       
      *       
      *

Enter  num: 6
Entered wrong input
     '''
