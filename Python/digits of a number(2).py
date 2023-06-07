Num=int(input("Enter a five digit number\n"))
x=10000
i=1
Remainder = Num
while i <= 5:
    Digit=(Remainder/x)
    Remainder = Num % x
    print(Digit)
    x=x/10
    i=i+1
