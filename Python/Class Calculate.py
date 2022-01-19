class calculate:
    def add(self,Num1,Num2):
        Sum=Num1+Num2
        return Sum
    def subtract(self,Num1,Num2):
        Diffrence=Num1-Num2
        return Difference
    def multiply(self,Num1,Num2):
        Product=Num1*Num2
        return Product
    def divide(self,Num1,Num2):
        Quotient=Num1/Num2
        return Quotient

Calculate=calculate
loop=0 

while loop==0:
    Menu=raw_input("Do you want to add, subtract, multiply, divide or quit calculator")
    Number1=int(input("Enter the first number"))
    Number2=int(input("Enter the second number"))
    
    if Menu=="add":
        print Calculate.add(Number1,Number2)
        print ""
    elif Menu=="subtract":
        print Calculate.subtract(Number1,Number2)
        print ""
    elif Menu=="multiply":
        print Calculate.multiply(Number1,Number2)
        print ""
    elif Menu=="subtract":
        print Calculate.subtract(Number1,Number2)
        print ""
    elif Menu=="quit":
        loop=1
        print "Thanks for using calculator"
    else:
        print "Error"
        print "Try again"
        print ""

exit()
