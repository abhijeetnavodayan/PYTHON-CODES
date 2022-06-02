import numpy as p
l=list(map(int,input("enter a no.").split()))
r=l[::-1]
a=p.array(r,dtype='float')
print(a)