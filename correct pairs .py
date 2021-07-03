num=list(map(int,input().split()))
cnt=0
for i in range(0,len(num)):
    for j in range (i,len(num)):
        if i<j and num[i]==num[j]:
            cnt+=1
print(cnt)


'''
1 2 3 1 1 3
4

4 2 3 1 6 3 2 
2
'''
