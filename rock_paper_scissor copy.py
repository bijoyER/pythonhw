import random
print("welcome to childhood game rock_paper_seizer.")

while True:
    user=input("Your trun:")
    cls=["rock","paper","seizer"]
    computer=random.choice(cls)
    print("computer action is:",computer)
    if user==computer:
       print("this is a tie.")
    elif user!="rock"and"paper"and"seizer":
        print("your input is wrong.Try again.")
    elif user=="rock" and computer=="paper"or user=="seizer"and computer=="rock"or user=="paper"and computer=="seizer":
        print("comter win")
    #elif user=="seizer"and computer=="rock":
        #print("computer win")
    #elif user=="paper"and computer=="seizer":
        #print("computer Win")
    else:
        print("you win")
    
    print("\nDo you want to play a gain:(y/n)")
    dec=input("y or n:")
    if dec.lower()=="y":
        print("play aganin")
        
    else:
        print("to play input y")
        break
print("thanks for playing.\n")