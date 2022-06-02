d={"ram":{"salery":10000,"age":19,"height":6},
    "shyam":{"salery":20000,"age":18,"height":5.6},
    "laxman":{"salery":2003,"age":19,"height":5} 
     }
lst=[]
for i in d.values():
    lst.append(i["salery"])
print("maximum salery:",max(lst))
print("minimum salery:",min(lst))     