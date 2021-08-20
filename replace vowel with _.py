n=input('Enter String :')
char=input('Enter character: ')
for i in n:
    if i in 'aeiouAEIOU':
        n=n.replace(i,char)
print(n)

'''
Enter String :Avengers
Enter character: *
*v*ng*rs
'''

n=input('Enter String :')
s=' '
for i in n:
    if i in 'aeiouAEIOU':
        s+='_'
    else:
        s+=i

print(s)

'''
Enter String :Iron man
 _r_n m_n
 
'''
