#The methode exit() is imported to make exit() work.
#exit() is like a synonym of quit(). 
#You can add a message to exit(), for example to let the user know why a script stops. 

from sys import exit



#Note: The function gold_room is the first function defined. But the program doesn't start with this function. 
#This program starts with function start(). See this function in the end of the code.
#gold_room will run when certain condition in function bear_room() is True.
def gold_room():
    print("This room is full of gold. How much do you take?")
    
    #There are no restrictions here for input.
    choice = input(">")
    
    #If choice is a number and the number contains: 0 or 1 ---> "Nice, you're not greedy, you win!" or  "You greedy bastard!"
    #Note: this means that if choice == 66 also triggers: dead("Man, learn to type a number."
    #If alphabetic characters are entered: dead("Man, learn to type a number."
    #Note: if a combination of numbers and alphabetic characters are entered ---> error     
    if "0" in choice or "1" in choice:
        
        how_much = int(choice)
    
    
    else:
        dead("Man, learn to type a number.")
 
    if how_much < 50:
        #If input is smaller than 50, copy below will be printed and the program will exit.
        print("Nice, you're not greedy, you win!")
        
        
        exit(0)
        
    else:
        #If input is larger than 50, the function dead(why) will run program will exit.         
        dead("You greedy bastard!")
 

#This function depends on function start()  
def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    
   
    bear_moved = False
    
    #Creates an infinite loop.
    while True:
          
        choice = input(">")
        
        # Input has to be igual to 'take honey'. Note: case sensitive.
        if choice == "take honey":
            #function dead(why) will run when condition is met and program will exit. 
            dead("The bear looks at you then slaps your face off.")
        
        #Variable bear_moved = False. This means that: elif choice == "taunt bear" and not False (not False = True) 
        #If choice == "taunt bear" (if user enters "taunt bear") the elif statement will be True.
        #Note: there is no clue for users that they have to enter "taunt bear" to take them to next step.
        #Next step is elif choice == "open door" and bear_moved".
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
                
            #The bear_moved variable is now True.
            #This variable applies to the function's elif statements below.
            bear_moved = True
        
    
        #Variable bear_moved = True -> elif choice == "taunt" bear and True.  
        #If choice == "taunt bear", elif statement will be True and function dead(why) will run.
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews yoor leg off.")
        
       
        #Note: Variable bear_moved = True -> elif choice == "open door" and True. 
        #If choice == 'open door' the function gold_room will run.
        #Note: There is no clue for users that they have to enter 'open door' to take them to the next  lead to gold_room.
        elif choice == "open door" and bear_moved:
            gold_room()
        
        #elif choice != not "taunt bear" and elif choice != open door:
        else:
            print("I got no idea what that means.")
                
#This function is triggered when choice == right in function start()                
def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")
                    
    choice = input("> ")
    
    #If choice contains "flee" function start() will run again.
    #The in operator is more flexible. If users enter "flee now" or "flee!" it works.
    #But this statement also triggers: flees, fleehsgshe, sffleemddn, etc.  
        
    if "flee" in choice:
        start()
    
     #If choice contains "head" function dead() will run and program will exit.
    elif "head" in choice:
        dead("Well that was tasty!")
    
    #If choice is something else than "flee" or "head", the function cthulhu_room() starts again.
    else: 
        cthulhu_room()
        

        
def dead(why):
    print(why, "Good job")
    
    exit(0)


#Program starts with this function and can also be triggered by function cthulhu_room():
def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do yo take?")
    
    choice = input(">")
    
       
    if choice == "left":
        bear_room()
   
    elif choice == "right":
        cthulhu_room()
    else:
    #The dead function will run.
        dead("You stumble around the room until you starve.")
        
    
start()
                        
                        
                
    
   