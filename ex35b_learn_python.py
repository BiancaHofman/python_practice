from sys import exit 

#I changed the script ex35 to create the script ex35b.py. Below you'll find a overview of the changes I made. 

#Changes in order of functions  
                              #---> I changed the order of the various functions a bit, to make the code easier to read. For example, the function start() is now in the beginning and not in the end.
                              #---> I created a new function: cthulhu_room_stuck():


#Changes in if, elif and else statements 
                    # ---> in all statements I added .lower() which translates input to lowercase using the built-in "lower" string function.   
                    # ---> in bear_room, I deleted the elif condition, becaus they were not needed anymore.   
                    # ---> in cthulhu_room I changed the 'if in' into == to deal with typos etc. I'm searching for a better solution.
                    # ---> in gold_room I added numbers to the if conditions, to make  I still need to improve this, to make the code less repetitive. 
                    # ---> in some statements the code is repetitive, because I tried to use parentheses and it didn't work. I still need to work on these ones.
                           
                                        

#Change in copy 
                 # ---> I changed the story a bit.
                 # ---> I added and changed copy to help the user make choices, to make the flow more clear and to add extra emotion. 
                 # ---> For example: In dead(why) I changed 'good job' into 'game over', I added exclamations and changed the questions a bit.
                 
                 
      
                                 

def start():
    print("'Every door is another passage, another boundary we have to go beyond.'")
    print("That's what Rumi wrote.")
    print("So, go for it.") 
    print("Which door do you choose? Left or right?")
   
    
   
    choice = input(">") 
   
    
    if "left" == choice.lower():
        bear_room()
   
    elif "right" == choice.lower():
        cthulhu_room()
    else:
        dead("That didn't work out. Your story ends before it even begins.")

        
def dead(why):
    print(why, "Game over")
    exit(0)


def bear_room():
    print("Aaaah! There is a huge bear in this room!")
    print("He sits right in front of the exit door.")
    print("You almost stumble over his pile of honey.")
    print("He is staring at you in a hostile way.") 
    print("Okay, this is not Winnie the Pooh.")
    print("What do you do?")
    print("Do you eat some honey or...")
    print("...do you remain still and wait?") 
       
   
    bear_moved = False
    
    while True:
          
        choice = input(">")     
        
        
        if "eat honey" == choice.lower() or "eat the honey" == choice.lower() or "honey" == choice.lower() or "eat it" == choice.lower():
            dead("That was not a smart move. The bear is pissed off now and you'll be his snack.")
     
   
        elif ("remain" == choice.lower() or "wait" == choice.lower() or "remain still" == choice.lower() or "remain still and wait" == choice.lower()) and not bear_moved:
            print("Clever! The bear has moved from the door.")
            print("Avoid eye contact. Walk slowly to the exit.")
            print("Uhh...oops...the door is locked.")
            print("No time to lose. Use the magic words: open sesame.")          
            
            bear_moved = True                
      
        elif "open sesame" == choice.lower() and bear_moved:
            gold_room()
        
        else:
            dead("This was not an option. You'll be a bear's snack.")

               
def cthulhu_room():
    print("Ohh...You've entered the room of the great evil Cthulhu.")
    print("Better keep your eyes closed.")
    print("Because those who look at Cthulhu will go insane.")
    print("Do you flee or fight?")
                    
    choice = input("> ")
   
   
    if "flee" == choice.lower():
        print("Smart!") 
        print("Because this is your chance to start all over again!")
        start()
    
    elif "fight" == choice.lower():
        print("Fight? You've lost your sanity!") 
        print("Or did you try to be a hero?") 
        dead("Well, you are a hero, but a dead one.")
    
    else: 
        print("This won't get you out of Cthulhu's room.")
        cthulhu_room_stuck()

def cthulhu_room_stuck():
    print("Let's face it. You are stuck in a room with this evil creature.")
    print("You'll go insane. It's sad, but your story ends here.")
    
    exit(0)

def gold_room():
    print("Yes! Hurray! You've entered the Gold Room.") 
    print("The room is full of coins.")
    print("But shhh, please be quiet.") 
    print("You don't want to wake up the guardian.")
    print("And be quick. You cannot hang around here for too long.")
    print("How many coins do you take?")

    choice = input(">")
    
    if "0" in choice or "1" in choice or "2" in choice or "3" in choice or "4" in choice or "5" in choice or "6" in choice or "7" in choice or "8" in choice or "9" in choice: 
    
        how_much = int(choice)    
        
    else:
        dead("Geez! Learn to type a number. There is no time for letters and nonsense. Your story ends here.")  
 
    if how_much < 50:
        print("Nice, you're not greedy and YOU ARE A WINNER.")
        print("The story ends here. Now go, before you wake up the guardian.")       
        
     
        exit(0)            
        
    elif how_much > 50:
        print("You greedy bastard!")
        print("And while you were so busy collecting all these coins...")
        dead("...the guardian woke up. Your story ends here.")   
        
    
start()
                        
                        
                
    
   