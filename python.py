#A1
x = int(input("enter a number"))
if len(str(x)) == 3 :
     print("True")
else:
    print("False")
    
#A2
age = int(input("enter your age"))
if(age>18):
    print(age,"can vote")
else:
    print(age,"can't vote!!!!")

#A3
age1 = int(input("enter your age"))
if(age1>=65):
    print(age1,"Senior Citizen")
else:
    print("young people")

#A4
a = int(input("enter 1st number"))
b = int(input("enter 2nd number"))
if(a>b):
    print(b,"is the smaller number")
else:
    print(a,"is the smaller number")

#A5
a1 = int(input("enter 1st number"))
b1 = int(input("enter 2nd number"))
if(a1>b1):
    print(a1,"is the largest number")
else:
    print(b1,"is the largest number")
    
#A6
num = int(input("enter a number"))
if(num<0):
    print(num,"is negative")
else:
    print(num, "is positive")
    
#A7
num1 = int(input("enter a number"))
if(num1%2==0):
    print(num1,"is even")
else:
    print(num1,"is odd")

#A8
number_names=["Zero","One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

num2= int(input("enter a number:"))
print(number_names[num2])

#A9
num3 = int(input("Please enter a number: "))

if num3%6==0:
    print("{} is divisible by both 2 and 3".format(num3))
else:
    print("{} is not divisible by both 2 and 3".format(num3))
    
#A10
p = int(input("Enter first number: "))
q = int(input("Enter second number: "))
r = int(input("Enter third number: "))
 
if (p > q) and (p > r):
  print("The largest number is",p)
elif (q > p) and (q > r):
  print("The largest number is",q)
else:
  print("The largest number is",r) 

