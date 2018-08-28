t=int(input())
if(t<=1000):
   for i in (2,t):
       r=t%i
       if(r==0):
          print(r)
          break
else:
   print('no')
