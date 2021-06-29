a=list(map(int,input().split()))
for i in range(0,len(a)):
    for j in range(i,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print('After Sorting',a)


          '''
6 4 1 8 3 9
After Sorting [1, 3, 4, 6, 8, 9]

          '''
