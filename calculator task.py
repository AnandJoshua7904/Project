def add(x,y):
    return x+y

def sub(x,y):
    return x-y 

def multi(x,y):
    return x*y

def div(x,y):
    if y==0:
       return "error '0' cannot be divisable"
    else:
        return(x/y)
    
print("Select method")
print("1 Add")
print("2 Sub")
print("3 Multiplication")
print("4 Division")

while True:
    choose=int(input('Enter choice(1/2/3/4)'))

    if choose in (1,2,3,4):

        num1=int(input('enter your first number'))
        num2=int(input('enter your second number'))


        if choose==1:
            print("result:",add(num1,num2))
        elif choose==2:
            print("result:",sub(num1,num2))
        elif choose==3:
            print("result:",multi(num1,num2))
        elif choose==4:
            print("result:",div(num1,num2))

        break    

    else:
        print("invalid input")