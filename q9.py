# Q.9 Apki pass ek shopping name ki ek dictionary hai
import json
d={}
a=int(input("ente the size of main dictionary"))
for i in range(a):
    key=input("enter the name of main dict")
    size=int(input("enter the size of nested dict"))
    c={}
    for j in range(size):
        n=(input("enter the key"))
        value=input("enter the name of value")
        c[n]=value
    d[key]=c
t=open("raja.json","w")
h=json.dump(d,t,indent=6)