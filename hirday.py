num1=(float(input("enter the first number")))
num2=(float(input("enter the  second number ")))
print("press 1 for addition\n press2 for subtraction\n press 3 for multiplication\n press 4 for division")
choice=(int(input("enter your choice")))
if choice==1:
    print( "the addition is",num1+num2)
elif choice==2:
    print( "the subtraction is",num1-num2)
elif choice==3:
    print("the multiplication is ",num1*num2)
else:
    print("the division is",num1/num2)
