a=input("Enter String: ")
sum=0
for i in a:
    if a.isdigit()== True:
        sum+=int(i)
    else:
        break

print(sum)
        
'''
Enter String: 12345
15
'''
