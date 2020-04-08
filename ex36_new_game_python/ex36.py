from sys import argv 
from sys import exit

#user_name refers to the name of the person who is reading the story. 

#filename_grandmother is the story that will be printed if user makes a certain choice in function attic().

#filename_kitchen is content that will be printed when the function kitchen() starts to run.

#filename_attic is the content that will be printed when function attic() starts to run.


#filename_grandmother = granny.txt
#filename_kitchen = kitchen.txt
#filename_attic = attic.txt

script, filename_grandmother, filename_kitchen, filename_attic, user_name = argv


def start():        
    print(f"{user_name}, it's 02.43 AM and you are awake.")
    print("The early birds are still sleeping!")
    print("Do you stay in bed?")
    
    #lower() will convert the user input always into lower case, to make sure it doesn't matter if input is in lower case or not.
    choice = input(">")
    
    if choice.lower() == "yes" or choice.lower() == "yeah":
        print("You stay in bed, but you'll be staring at the ceiling until your alarm goes off.")
        insomnia_wins()                
    
    elif choice.lower() == "stay in bed" or choice.lower() == "yes, stay in bed":
        print("You stay in bed, but you'll be staring at the ceiling until your alarm goes off.")
        insomnia_wins() 
    
    elif choice.lower() == "no":
        print("You shuffle to your bedroom door.")
        print("Do you go to the the kitchen or the bathroom?")
        
        choice = input(">")
        
        if choice.lower() == "kitchen":
            kitchen()    
        
        elif "go to kitchen" == choice.lower():
            kitchen()
        
        elif "go to the kitchen" == choice.lower():
            kitchen()
        
        elif choice.lower() == "bathroom":
            bathroom()
        
        
        elif "go to bathroom" == choice.lower():
            bathroom()
        
        elif "go to the bathroom" == choice.lower():
            bathroom()
        
        else:
            print("Just choose bathroom or kitchen.")
            start()
    
    else:
        print("Just keep it simple and answer yes or no.")
        start()                
    
#In function kitchen(), I also use text documents to print content.
#I did this to practise.
#I assume it is better to avoid too much printed text in the script intself, for maintenance reasons.
#For now, I didn't worry too much about that, but I'll do more investigation on this topic.
def kitchen():
    
    text = open(filename_kitchen)
    print(text.read())
    
    choice = input(">")     
     
    if choice.lower() == "pie":
        print("That pie was delicious!")
        print("Now back to bed!") 
        print("...wait...what's that sound?")   
        print("Is that the attic floor creaking?") 
        print("Footsteps?") 
        print("Nooo, that's must be your imagination.")
        print("Or not?") 
        print("Do you go back to bed or do you go to the attic?")
        
        choice = input(">")
        
        if "bed" == choice.lower() or "go back to bed" == choice.lower():
            print("You ate too much pie.")        
            insomnia_wins()
            
        elif "attic" == choice.lower():
            attic()
        
        elif "go to attic" == choice.lower() or "go to the attic" == choice.lower():
            attic()
   
        
        else:
           print("Just answer bed or attic.")
           kitchen()
           

    elif choice.lower() == "rooibos":
        print("Rooibos is a herbal tea from South Africa.") 
        print("Some say it helps to improve sleep.") 
        print("Not sure if that's true.")
        print("But it seems to work for you.")
        print("Sweet dreams!")
        sleep_exit()    
   
 
    else:
        print("Just say Rooibos or pie")     
        kitchen()

def bathroom():
    print("You are in the bathroom.")
    print("You've just flushed the toilet when you hear something falling.")
    print("The cat is probably climbing the bookshelves again.")
    print("Do you want to check what your cat has done?") 


    choice = input(">")

    if "yes" == choice.lower():
        print("Okay let's go to the living room.")        
        living_room()
    
    elif choice.lower() == "no":    
        print("Okay")
        print("Yeah, you might be right.")
        print("It's way too early to check out what the cat is doing.")
        print("It's time to sleep.")        
        sleep_exit()  

    else:
        print("Just answer yes or no. Otherwise you'll be stuck in the bathroom all night.")
        bathroom()    
            

#In function attic(), I also use text documents to print content.
#I did this to practise.
#I assume it better to avoid too much printed text in the script itself, for maintenance reasons.
#For now, I didn't worry too much about that, but I'll do more investigation on this topic. 
def attic():
    text = open(filename_attic)
    print(text.read())
   
    choice = input(">")
   
    if choice.lower() == "flee":
        print("You run down the stairs and jump back into your bed.")
        print("In bed you try to convince yourself this was just your imagination.")
        print("You'll be staring at the ceiling until your alarm goes off.")
        insomnia_wins()
        
        
    elif choice.lower() == "listen":
        print("Do you want to listen to your grandfather or your grandmother?")    
   
        choice = input(">") 
        
        
        txt = open(filename_grandmother)
   
        if choice.lower() == "grandmother" or choice.lower() == "listen to grandmother":
            print("The creepy voice starts to recite a poem.")
            print("----------------------------------------------") 
            print(txt.read())
            print("----------------------------------------------") 
            print("This was not your beloved granny.")
            print("This was the ghost assistant of Insomnia reciting a scary poem.")
            print("She helps Insomnia by keeping people awake.")       
            print("You run down the stairs...")
            print("...and jump into your bed.") 
            print("You'll be staring at the ceiling until you alarm goes off.") 
            print("And you'll get up on the wrong side of the bed.")        
            insomnia_wins()
    
        elif choice.lower() == "grandfather" or choice.lower() == "listen to grandfather":
            print("Your grandfather was a lovely man and you have to admit he's a friendly ghost.") 
            print("His story bores you to sleep, though...")
            print("...and the other creepy voice disappeared.")
            sleep_exit()  

        
        else:
            print("Just answer granny or grandfather or you'll be stuck in this attic forever.")
            attic()
   
    else:
        print("Just answer flee or listen, if you don't want to be stuck in this attic forever.")
        attic()
        
def living_room():
    print("Yes, it was the cat again.") 
    print("He is hiding behind a plant on the top shelf.")
    print("And some of your books fell on the floor.")
    print("Do you pick up the books?")
    print("Or do you go to the garden to get some fresh air?")
    
    
    choice = input(">") 
    
    if "garden" == choice.lower():
        garden()
        
    elif "go to the garden" == choice.lower() or "go to garden" == choice.lower():
        garden()
       
    
    elif choice.lower() == "books":
        print("Your cat dropped the book 'Bedtime stories for stressed out Adults' on the floor.")
        print("'Tales to soothe tired souls' it says, by Lucy Mangan")
        print("Wow. You didn't remember you had that book.")
        print("You take it and you go back to bed. Thanks cat!")
        sleep_exit()
    
    elif choice.lower() == "pick up the books" or choice.lower() == "pick up books":
        print("Your cat dropped the book 'Bedtime stories for stressed out Adults' on the floor.")
        print("'Tales to soothe tired souls' it says, by Lucy Mangan")
        print("Wow. You didn't remember you had that book.")
        print("You take it and you go back to bed. Thanks cat!")
        sleep_exit()

    
    else:
        print("Just answer garden or books, if you don't want to be stuck in the living room forever.")
        living_room()
        

def garden():
    print("Your crazy neighbour is walking in your garden with a flashlight.")
    print("Do you ignore the man or talk to him?")    

    choice = input(">") 
    
    if choice.lower() == "ignore" or choice.lower() == "ignore the man":
        print("You ignore him.")
        print("The man is crazy but harmless.")
        print("Last week he saw aliens on your roof terrace.") 
        print("He'll go back to his own place, when he gets tired.")
        print("You'll go back to bed for a bit more sleep.") 
        sleep_exit()
    
    elif choice.lower() == "ignore him":
        print("You ignore him.")
        print("The man is crazy but harmless.")
        print("Last week he saw aliens on your roof terrace.") 
        print("He'll go back to his own place, when he gets tired.")
        print("You'll go back to bed for a bit more sleep.") 
        sleep_exit()
    
    elif choice.lower() == "talk" or choice.lower() == "talk to him":
        print("You ask your neighbour what he's doing in your garden, in the middle of the night.")
        print("The man is crazy, but harmless.")
        print("Last week he saw ghosts on your roof terrace.") 
        print(f"'{user_name}, this night I've seen a man and a woman staring through your attic's window!', he says.") 
        print("Pfff. You explain your neighbour that there is nobody else in the house apart from you.")
        print("But back in bed, you start to get a bit nervous, though.")
        print("What if your neighbour is not crazy...")
        insomnia_wins()
        
        
    else:
        print("Just answer talk or ignore, if you don't want to be stuck in the garden forever.")
        garden()

def sleep_exit():
    print("You'll sleep like a baby. Insomnia lost. You won! THE END")
    exit(0)

    
def insomnia_wins():
    print("Insomnia wins. You lose. GAME OVER")
    exit(0)

start()
