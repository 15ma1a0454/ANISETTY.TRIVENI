r=int(input())
if(r<=1000):
   for i in (2,r):
       t=r%i
       if(t==0):
          print('no')
          break
       else:
         print('yes')
         break
else:
   print('no')
