n=int(input())
rem=0
s=''
while True:
    rem=n%2
    print(rem)
    s=s+str(rem)
    n=n//2
    if n<=1:
        print(1)
        s+=str(1)
        break
if len(s)<4:
    print(0)
else:
    print('4th bit',s[3])

'''
12
0
0
1
1
4th bit 1

23
1
1
1
0
1
4th bit 0
'''
