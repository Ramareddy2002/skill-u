candies=list(map(int,input().split()))
a=[]
extra_c=int(input('Enter extra candies:'))
for i in range(len(candies)):
    if i+extra_c>=max(candies):
        a.append(True)
    else:
        a.append(False)
print(a)

    '''

2 4 1 5 3 
Enter extra candies:3
[False, False, True, True, True]

    '''
