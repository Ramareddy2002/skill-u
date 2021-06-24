def cp(n):
    if n==0 or n==4 or n==6 or n==9:
        return 1
    elif n==8:
        return 2
    else:
        return 0
def cpsum(t):
    s=0
    while t:
        rem=t%10
        t=t//10
        s+=cp(rem)
    return s
t=int(input())
print(cpsum(t))
    
'''
630  # entered number
2 #no of closed paths

12344
2

64598
5
'''
