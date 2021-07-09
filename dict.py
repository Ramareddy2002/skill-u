a={}
n=int(input('enter number of students:'))
for i in range(n):
    x=input('enter student name:')
    y=list(map(int,input('enter marks:').split()))
    a[x]=y
    print(a)


'''
enter number of students:3
enter student name:Harry
enter marks:10 20 30
{'Harry': [10, 20, 30]}
enter student name:Ron
enter marks:30 10 15
{'Harry': [10, 20, 30], 'Ron': [30, 10, 15]}
enter student name:Hermoine
enter marks:100 100 90
{'Harry': [10, 20, 30], 'Ron': [30, 10, 15], 'Hermoine': [100, 100, 90]}

'''
