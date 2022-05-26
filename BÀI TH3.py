#BÀI TH 3
#1
def sum(a,b):
    print("sum="+str(a+b))
#tinh tong 2 so 9,8
sum(9,8)
#tinh tong 2 so 2,7
sum(2,7)

#2
def sum(a,b):
    return a+b
c=sum(4,5);
print("tong của 4 va 5 la: "+ str(c))

#3
def say_hello():
  a=("hello")
  print(a)
say_hello()
print(a)

#4
a="hello guy!"
def say(a):
    a="VINH UNIVERSITY"
    print(a)
say(a)
print(a)

#5
a="hello guy!"
def say():
    global a
    a="VINH UNIVERSITY"
    print(a)
say()
print(a)

#6
def get_sum(*num):
    tmp=0
    #duyet cac tham so
    for i in num:
        tmp +=i
    return tmp
result=get_sum(1,2,3,4,5)
print(result)

#7
def checkValue(n):
    if n%2==0:
        print("dây là số chẵn")
    else:
        print("đây là số lẻ")
checkValue(7)


#8
import math
pos=[0,0]
while True:
    s=input()
    if not s:
        break
    movement=s.split(" ")
    direction=movement[0]
    steps=int(movement[1])
    if direction=="UP":
        pos[0]+=steps
    if direction=="DOWN":
        pos[0]-=steps
    elif direction=="LEFT":
        pos[0]-=steps
    elif direction=="RIGHT":
        pos[0]+=steps
    else:
        pass
    ##################
    print(int(round(math.sqrt(pos[1]**2+pos[0]**2))))

#9
#this funtion adds two numbers
def add(x,y):
    return x+y
#this funtion subtracts two numbers
def subtract(x,y):
    return x-y
#this funtion multiplies two numbers
def multiply(x,y):
    return x*y
#this funtion divides two numbers
def divide(x,y):
    return x/y
print("select operation.")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")

#take input from the user
choice=input("enter choice(1/2/3/4):")
num1=int(input("enter first number:"))
num1=int(input("enter second number:"))

if choice=='1':
    print(num1,"+",num2,"=",add(num1,num2))
elif choice=='2':
     print(num1,"-",num2,"=",subtract(num1,num2))
elif choice=='3':
     print(num1,"*",num2,"=",multiply(num1,num2))
elif choice=='4':
     print(num1,"/",num2,"=",devide(num1,num2))
else:
    print("invalid input")

