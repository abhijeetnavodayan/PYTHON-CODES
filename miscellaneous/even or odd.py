a=[]
size=int(input("length of string"))
for i in range(size):
    val=(int(input("enter numbers")))
    a.append(val)
even=0
odd=0
for i in range(size):
    if(a[i]%2==0):
        even=even+1
    else:
        odd=odd+1
print("even=",even,"odd=",odd)
