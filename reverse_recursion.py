n=int(input('Enter a number: '))
rev=0
def reverse_rec(n):
    global rev
    if(n!=0):
        rem=n%10
        rev=rev*10+rem
        reverse_rec(n//10)
        return rev

rev=reverse_rec(n)
print('reverse=%d'%rev)

'''
Enter a number: 2341
reverse=1432

Enter a number: 54321
reverse=12345

'''
