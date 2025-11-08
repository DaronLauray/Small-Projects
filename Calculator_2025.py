print('Calculator using Python-Daron Lauray')
# A simple calculator that can be customized for any calculation
value= input(' what do you want to do?: +,-,*, or /')
a= int(input('first number'))
b= int(input('second number'))
atot= float(a+b, 3)
stot= float(a-b, 3)
mtot= float(a*b, 3)
dtot= float(a/b, 3)

def add():  
    print(atot)
def subtract():
    print(stot)
def multiply():
    print(mtot)
def divide():
     print(dtot)
if value is "+":
    add()
elif value is "-":
    subtract()
elif value is "*":
    multiply()
elif value is "/":
    divide()
else: print( 'input the function without spaces')