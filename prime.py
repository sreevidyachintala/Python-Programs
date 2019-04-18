#prime number generation
sum=0
l=int(input('enter the starting number: '))
u=int(input('enter the ending number: '))
print("Prime numbers between",l,"and",u,"are:")
for i in range(l,u+1):
   if l>1:
      for j in range(2,i):
         if i %j==0:
            break
      else:
         sum=sum+i
         print(i,end=' ,')
print('\nsum is',sum)
      
