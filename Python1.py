a= int(input("enter the no: "))
b=int(input("enter the no: "))
c=int(input("enter the no: "))
print("Enter your choice")
print("1= Greater number\n",
      "2= Lower number\n",
      "3=Addition\n",
      "4=multiplication\n")
check=int(input("enter your choice: "))
if check==1:
    print("Greater Number is: ",max(a,b,c))
elif check==2:
    print("lower number is: ",min(a,b,c))
elif check==3:
    print("Addition is: ",a+b+c)
elif check==4:
    print("Multiplication is: ",a*b*c)
else:
    print("Invalid choice")
    
    
