import random                   
Random=random.randrange(1000,10000) #Generating a random number (4-digit)

Divide=1000                         #Finding its digits
loop1=1
Remainder = Random
Number1=[]
while loop1<= 4:
    Digit=(Remainder/Divide)
    Remainder = Random % Divide
    Number1.append(Digit)            #Entering the Digits in a list
    Divide=Divide/10
    loop1=loop1+1

loop2=0
loop3=0

while loop2==0:
    User=int(input("What do you think the four digit number is?")
    Divide=1000
    loop1=1
    Remainder=User
    Number2=[]
    Digit=0
    while loop3<= 4:
        Digit=(Remainder/Divide)
        Remainder=Random%Divide
        Number2.append(Digit)
        Divide=Divide/10
        loop3=loop3+1
    for Num1 in Number1:
        for Num2 in Number2:
            if Num1==Num2:
             Count=Count+1
    print "You got," , Count , "numbers correct!"
    if User==Random:
        print "You got it!!! :)"
        print "The number is, " , Random , "!"
        print "Do you want to play again?"
        loop2=1 

