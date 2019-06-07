n1,n2=[int(n1) for n1 in input().split()]
b=range(n1,n2)
list=[]
for c in b:
    if((c>n1) and (c<n2)):
        if(c%2!=0):
            list.append(str(c))
d=' '.join(list)
print(d)
