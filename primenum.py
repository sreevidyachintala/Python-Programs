# Python program to check if the input number is prime or not
# take input from the user
n = int(input("Enter a number: "))

# prime numbers are greater than 1
if n > 1:
   for i in range(2,n):
       if (n % i) == 0:
           print(n,"is not a prime number")
           #print(i,"times",num//i,"is",num)
           break
   else:
       print(n,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(n,"is not a prime number")
