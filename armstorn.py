def armstrong(n,s=0):
    l=len(str(n))
    s=0
    t=n
    while n>0:
        r=n%10
        s+=r**l 
        n=n//10 
    if t==s:
        return "armstrong" 
    return "not armstrong"

n=int(input())
print(armstrong(n))
