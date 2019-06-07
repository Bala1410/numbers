n1,n2=list(map(int,input().split()))
b=range(n1+1,n2)
for a in b:
 k=0
 for i in range(2,a//2+1):
  if(a%i==0):
   k=k+1
 if(k<=0):
  print(a,end=" ")
