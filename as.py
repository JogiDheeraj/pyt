n=int(input())
l=len(str(n))
s=0
t=n
while n>0:
    r=n%10
    s+=r**l 
    n=n//10 

if t==s:
    print("armstrong")
else:
    print("not armstrong")

