t=int(input())
fact=1
if(t<0):
    print('sorry factorial does not exist for negative numbers')
elif(t==0):
    print('1')
else:
    for i in range(1,t+1):
         fact=fact*i
    print(fact)
