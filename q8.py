# Q8.Tumhare pass four employes ki details hai list mai:-
import json
d={}
a=int(input("enter the size of main dictionary"))
for i in range (a):
    key=input("enter the key name of main dictionary")
    size=int(input("enter the size of nested dict"))
    c={}
    for j in range(size):
        n=input('enter the name of key')
        value=input('enter the value:')
        c[n]=value
    d[key]=c
f=open("priya.json","w")
k=json.dump(d,f,indent=4)
    
