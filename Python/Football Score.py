def Tournament():
    Tournament=raw_input("Enter the name of the tournament")
    return ""

def Team_info():
    Teams=[]
    Team=" "
    loop=0
    print "Press Enter after entering all the team's names"
    while Team!="":
        if Team!=" ":
            Teams.append(Team)
        Team=raw_input("Enter the team's name")
    print "The teams are:"
    for x in Teams:
        print x
    print ""
    for i in Teams:
        print i , ":"
        Win=int(input("How many games has the team won"))
        Draw=int(input("How many games has the team drawn"))
        Lose=int(input("How many games has the team lost"))
        Score=0
        Score=Score+(Win*3)
        Score=Score+Draw
        Score=Score-Lose
        print "The team" , i , "has" , Score , "points"
    return ""   
    

def tournament_info():
    print Tournament()
    print Team_info()
    return ""

print tournament_info()
