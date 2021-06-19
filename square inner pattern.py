n=int(input('Enter an odd num: '))
if n%2!=0:
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(i==1 or i==n or i==n//2+1 or  j==1 or j==n or j==n//2+1):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
else:
    print('You have entered wrong number')

    '''
Enter an odd num: 7
* * * * * * * 
*     *     * 
*     *     * 
* * * * * * * 
*     *     * 
*     *     * 
* * * * * * *

Enter an odd num: 8
You have entered wrong number

    '''
