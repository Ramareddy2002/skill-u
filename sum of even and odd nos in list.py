a=list(map(int,input().split()))
sum_even=0
sum_odd=0
for i in a:
    if i%2==0:
        sum_even+=i
    else:
        sum_odd+=i
print('sum of even :',sum_even)
print('sum of odd :',sum_odd)

    '''
2 5 1 8 3 0 6 7 9
sum of even : 16
sum of odd : 25

    '''
