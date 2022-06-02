print "Jack=11"                                       #Introdcution
print "Queen=12"
print "King=13"
print "Ace=1"

                                                      #User starts playing

def deal_user():                                      #Create a function to deal cards to the user
    print "Your card is:"
    import random
    return random.randrange(1,14)
total_user=0                                          #Create a variable for the total of the user's cards
loop=0
Card=0                                                #Create a variable for the value of the card

while loop==0:
    print""
    Option=raw_input("Do you want a card? y/n: ")       #Ask if the user wants to take another card
    if Option=="y":                                   #If user wants to continue
        Num1=deal_user()
        print Num1
        if Num1>10:
            Card=10
        elif Num1==1:
            Ace=int(input("Do you want ace to be 1 or 11?"))
            if Ace==1:
                Card=1
            elif Ace==11:
                Card=11
            else:
                print "Error, Invalid input"
                Card=1
                print "Ace is 1 by default"
        else:
            Card=Num1
        total_user=total_user+Card                    #Calculate the total
    elif Option=="n":                                             # If user doesn't want to continue
        print"Your turn is over"
        print "Your score is:\n" , total_user
        print ""
        print ""
        loop=1
    else:
        print "Invalid input"
        print "Try again"
    if total_user>21:                                 #If user is bust(>21)
        loop=1
        print ""
        print "You are bust"
        print "You lose. Do you want to play again?"
        import sys
        sys.exit()
                                                      #User stops playing
                                                      #Computer starts playing
total_comp=0

def deal_comp(comp):                                  #Computer gets dealt
    import random
    print "My card is: "
    return random.randrange(1,14)

while total_comp<=17:
    Num2=deal_comp(0)
    print Num2
    if Num2>10:
        Card=10
    elif Num2==1:
        ace=total_comp+11
        if ace<=21:
            Card=11
        else:
            Card=1
    else:
        Card=Num2
    total_comp=total_comp+Card

if total_comp>21:
    print "I am bust"
    print "Congragulations, you win! Do you want to play again?"
    import sys
    sys.exit()
else:
    if total_comp>total_user:
        print "My score is:" , total_comp
        print "You lose. Do you want to play again?"
        import sys
        sys.exit()
    elif total_user>total_comp:
        print "My score is:" , total_comp
        print "Congragulations, you win! Do you want to play again?"
        import sys
        sys.exit()
    else:
        print "We tie" , total_user , "-" , total_comp
        import sys
        sys.exit()
    
            
