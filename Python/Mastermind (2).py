print "Welcome to the game of Mastermind!"

def random():
    import random
    Random=random.randrange(1000,10000)
    return Random

def digits(Num):
    D1=Num/1000
    D2=(Num-D1*1000)/100
    D3=(Num-D1*1000-D2*100)/10
    D4=(Num-D1*1000-D2*100-D3*10)/1
    Digits=[D1,D2,D3,D4]
    return Digits    

def secret():
    Num=random()
    Secret=digits(Num)
    return Secret


loop=0
Score=0
Secret_Num=secret()
print 
while loop==0:
    User=int(input("What do you think the number is?"))
    User=digits(User)
    for check1 in Secret_Num:
        for check2 in User:
             if check1==check2:
                 Score=Score+1
    Score=Score/4
    if Score<=2:
         print "You have got" , Score , "digits in the number correct"
         print "Try again"
    elif Score==3:
         print "You have got" , Score , "digits in the number correct"
         print "You almost made it"
         print "Try again"
    elif Score>3:
          print "You have got" , Score , "digits in the number correct"
          print "Congragulations, you did it!"
          print "Do you want to play again?"
          loop=1
print secret()

