r = int(input())
v = int(input())
for e in range(r,v+1):
   if e > 1:
       for i in range(2,e):
           if (e % i) == 0:
               break
       else:
           print(e)
