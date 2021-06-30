a=list(map(int,input().split()))
sum_even=0
sum_odd=0
for i in range(0,len(a)):
    if i%2==0:
        sum_even+=a[i]
    else:
        sum_odd+=a[i]
print('sum of even indexes :',sum_even)
print('sum of odd indexes :',sum_odd)



       '''

2 5 13 8 6 7 
sum of even indexes : 21
sum of odd indexes : 20

       '''
