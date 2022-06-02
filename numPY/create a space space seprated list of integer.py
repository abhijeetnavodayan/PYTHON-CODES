import numpy as p
r=int(input("enter a row"))
c=int(input("enter a col"))
l=list(map(int,input("enter a no.").split()))
a=p.array(l).reshape(r,c)
print(a)