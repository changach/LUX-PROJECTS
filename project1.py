# python program to check if x is a perfect square
import math
 
# A utility function that returns true if x is perfect square
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x
 
 #prompt user to enter a number (n)
n=int(input("Enter a number: "))
sol1=5*(n*n)+4
sol2=5*(n*n)-4

 # n is Fibonacci if one of 5*n*n + 4 or 5*n*n - 4 or both
# is a perferct square
if isPerfectSquare(sol1) or isPerfectSquare(sol2):
     print(n,"Is a fibonacchi number")
else:
         print(n,"is not a fibonacchi number")
