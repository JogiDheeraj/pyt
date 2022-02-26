def palindrome(n,s=0):
    temp=n
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    if temp ==s:
        return "Palindrome"
    return "Not Palindrome"

n=int(input())
print(palindrome(n))

