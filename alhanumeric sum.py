a=input('Enter String: ')
sum=0
for i in a:
    if i.isalnum()==True:
        sum+=int(i)
        
print(sum)



'''
Enter String: abcd123
6
'''

a=input('Enter String: ')
sum=0
for i in range(len(a)):
    if a[i] in "123456789":
        s=int(a[i])
        sum=sum+s
print(sum)

'''
Enter String: abcd123
6
'''
