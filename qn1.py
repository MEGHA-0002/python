# 1.Print Hello World to the console 
print("Hello World")

# 2.Add two numbers and print the result
a=int(input('eneter first number: '))
b=int(input("eneter second number: "))
def add(x,y):
  sum=x+y
  return sum
print("The sum is:",add(a,b))

#3.square root of a number
import math
num=int(input("enter a number to find square root: "))
def square_root(n):
  sqrt=math.sqrt(n)
  return sqrt
print("The square root is:",square_root(num))

def sqraeroot(n):
  sqrtt=n**0.5
  return sqrtt
print("The square root is: " , sqraeroot(num))

#4.area of triange
import math
a=int(input("enter base of triangle: "))
b=int(input("enter height of triangle: "))
c=int(input("enter side1 of triangle: "))
def area (a,b,c):
  s=(a+b+c)/2
  area=math.sqrt(s*(s-a)*(s-b)*(s-c))
  return area
print("The area of triangle is:",area(a,b,c))

# 5.sole a quadratic equation
import cmath

a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))

def quadratic(a, b, c):
    d = (b ** 2) - (4 * a * c)
    root1 = (-b + cmath.sqrt(d)) / (2 * a)
    root2 = (-b - cmath.sqrt(d)) / (2 * a)
    return root1, root2

print("The roots of the quadratic equation are:", quadratic(a, b, c))

#6.swap two variables
x = input("Enter first variable: ")
y = input("Enter second variable: ")
def swap(x, y):
    temp=x
    x=y
    y=temp
    return x, y
print("After swapping: ", swap(x, y))

#7.check even or odd
num = int(input("Enter a number to check even or odd: "))
def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
print("The number is:", check_even_odd(num))

# 8.generate a random number
import random
def generate():
  num=random.randint(1,100)
  return num
print("The random number is:", generate())

#9.positive or negative or zero
num = float(input("Enter a number to check positive, negative or zero: "))
def check_pos_neg_zero(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"
print("The number is:", check_pos_neg_zero(num))

#10.leap year or not
year = int(input("Enter a year to check if it's a leap year: "))
def check_leap_year(y):
    if(y%4==0 & y%100!=0) or (y%400==0):
        return "Leap Year"
    else:
        return "Not a Leap Year"
print("The year is:", check_leap_year(year))

#11.largest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
def largest_of_three(x, y, z):
    if (x >= y) and (x >= z):
        return x
    elif (y >= x) and (y >= z):
        return y
    else:
        return z
print("The largest number is:", largest_of_three(a, b, c))

#12.factorial of a number
num = int(input("Enter a number to find its factorial: "))
def factorial(n):
    if(n==0 or n==1):
        return 1
    else :
        return  n*factorial(n-1)
print("The factorial is:", factorial(n))

# 13.fabanocci series
n=int(input("enter the number o terms"))
a=0
b=1
count=0
while count < n:
    print (a, end=" ")
    a,b= b,a+b
    count +=1

# 14 . prime number
n=int(input("enter the number"));
if (n<2):
    print("Not prime")
else:
    for i in range(2,n):
        if n% i == 0:
            print("not prime")
            break
    else:
            print("prime number")
# 15 .series of prime number
start=int(input("enter the starting"))
end= int(input("enter the end"))
for num in range (start ,end +1):
    if num<2 :
        continue
    for i in range(2,num):
        if (num%i==0):
            break
    else :
        print(num, end ='')

# 16. sum of natural numbers
n = int(input("Enter the number of terms: "))

def sumofnatural(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(sumofnatural(n))

# 17. armstrong number
n=int(input("enter the number"))
num=n
order=len(str(n))
sum=0
while n>0 :
    digit = n %10;
    sum += digit ** order
    n //= 10
if sum==num:
    print("Amstrong Number")
else:
    print("not amstrong")

# 18.Not amstrong number
start =int(input("enter the number"))
end =int(input("enter the number"))
for n in range (start,end+1):
    order=len(str(n))
    sum=0
    num=n
    while num >0:
        digit =num%10
        sum += digit ** order
        num //=10
    if sum==n :
        print(n,end ='')


#19.multiplication table
num =int(input("enter the number"))
for i in range (1,11):
    print (f"{num} x {i} = {num * i}")

# 20 .power of 2 using anonymous function
a= lambda x: 2 ** x
num =int(int("enter the power"))
print(f"2 ^ {num}= ",a(num))
print(a(num))