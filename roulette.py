# Recreation of Buckshot Roulette Game logic
# must have:
# Randomizes Amount of bullets each round + Randomizes amount of live/non live ammo.

# Must have 3 items:
# magnifying glass  [ Can see the current bullet in the shell
# Saw: [Does double damage]
# Handcuffs [ Chooses a person to skip turn ]
# Option to shoot yourself or shoot another person. If yourself, you go again
# Looses life when shot
# 5 lives total
# turns go clockwise
# 2 min players max 4
import random

#main data types
#1. dictionary:
#   player_name: lives
#2. random list of lives/non-live bullet ordering


def saw(player_name):
    name_lives[player_name] -= 2

def handcuffs():
    # give option for players to print list of player names and their lives
    while True:
        try:
            print("To see the list of player names, type 'show'")
            player_select = input("Otherwise select which player loses a turn")
            if player_select == "show":
                for key, value in name_lives.items():
                    print(f"{key}: {value}")
            for key,value in name_lives.items():
                if player_select == key:
                    return player_select
        except ValueError:
            print(f"Nice try bud, but no one named {player_select} is crazy enough to play this game")
            
    #return selected_player

def magnifier(count):
    #return current indexed value of random list
    return bullet_order[count]

def print_player_lives():
    for key, value in name_lives.items():
                print(f"{key}: {value}")

def print_player():
    for key in name_lives:
        print(f"{key}")

def init():
    global lives
    lives = 5
    global name_lives
    name_lives = {} #dictionary for player:lives pairs
    global num_players
    num_players=input("Enter the number of players [2-4]: ")
    num_players = int(num_players)
    #set up dictionary: player:lives value pairs
    for i in range(num_players):
        player_name = input(f"What is player {i}'s name?: ")
        name_lives[player_name] = 5
    return num_players


def opening_remark():
    print('''Today we will be playing a game of mortality, a game of guns and risks\nLet's play roulette.\nTo play the game, you need to know the rules of course\nYou have a few options for every turn\nEither shoot your neighbor or shoot yourself, that's really all there is to it\nYou'll either blow yourself up or the person next to you, your choice\nJust know that if you shoot yourself with an empty shell, its still your turn\nIf you shoot someone else or you shoot yourself with a loaded shell, it's the next player's turn\nNow I'm sure you're all eager to get started\nGive me some information and we'll begin muahahaha''')

def add_remark():
    print('''Now you each get a maximum of 5 lives. \nLoading your lives now...\nHere they are!''')
    print_player_lives()
    print('''We'll have a couple of rounds, around 5...if more than one of you survives somehow, you can split the money\nSharing doesn't sound so appealing, so I'm sure all of you will want the next person gone\nThese are the items and their descriptions:\nItem #1 - Saw:[ Inflicts double the damage if hit with a live bullet ]\nItem #2 - Handcuffs:[ Choose a player to skip their turn ]\nItem #3 - Magnifying glass:[ Cheat and view the current bullet in the chamber\nWell, that's all to it. I say let's get started.\nPlayer 0 gets to go first!''')
    

def ammo_setup():
    bullet_opt = ["live", "blank"]
    global num_bullet
    num_bullet = random.randint(2,6) #random integer between 2 - 6
    global bullet_order
    bullet_order = []
    for i in range(num_bullet+1):
        bullet = random.choice(bullet_opt)
        bullet_order.append(bullet)
    return num_bullet

def item_setup():
    item_opt = ["Magnifying Glass","Saw","Handcuffs"]
    player_item = [] #list of item for one player
    global dic_item
    dic_item = {} #key:value pair of player name: list of items
    for key in name_lives: #loop through the key in the name_lives dictionary, getting player names
        items = random.sample(item_opt, 3)
        dic_item[key] = items

def print_items():
    for key, value in dic_item.items():
                print(f"{key}: {value}")

def has_item(item):
     for key,value in dic_item.items():
        if isinstance(value, list) and item in value:
            return True

        
def clear_player():
     for key,value in list(name_lives.items()):
          if value <= 0:
                del name_lives[key]
                return True
                 
               
     

def main():
    opening_remark() #some print statements, instructions   
    while True:
        try:
            num_players = init() 
            print("You entered these player names: ")
            print_player()
            confirm = input("Are these player names correct? Enter 'y/Y/yes/Yes' for yes or any other key for no: ")
            if confirm == 'y' or confirm == 'Y' or confirm == "yes" or confirm == "Yes":
                break
        except ValueError:
            print("Uhum, that wasn't one of the options, let's try that again please")
    add_remark() #more print statement instructions
    for i in range(6): #5 rounds
        empty = False
        defeat = False
        print("Currently loading up the shells")
        num_bullet = ammo_setup()
        print(num_bullet)
        while num_players >= 2: #make sure there is more than 1 player left
            item_setup() #give 3 items per player
            print("Here are everyone's items: ")
            print_items()
            count = 0
            while True:
                 for key in list(name_lives):
                      current_bullet = bullet_order[count] #loads current_bullet
                      print(f"It's player {key}'s turn")
                      use_item = input("Would you like to use an item? y/n")
                      if use_item == 'n':
                           print("Here are the current players and their lives: ")
                           print_player_lives()
                           player_to_shoot = input("Now who do you want to shoot? (type your own name if you want to shoot yourself)")
                           if(current_bullet == "live"):
                                print("Bam, you hit!")
                                name_lives[player_to_shoot] -= 1
                                print("Here are the current players and their lives now: ")
                                print_player_lives()
                                
                           else:
                                print("Seems like it was a miss")
            
                           count+=1
                           print(f"The current count is now: {count}")
                           cleared = clear_player() # clear any players that have 0 lives left
                           if cleared == True:
                                num_players-=1
                           print(f"The current number of players is: {num_players}")
                        
                           if num_players < 2:
                        
                                defeat = True
                                break
                           if(count >= num_bullet): #if the count becomes more than the num_bullets, break out of loop and round is over
                                print("Seems that the racks are empty")
                                empty = True
                                break
                 
                      if use_item == 'y':
                           print("Here are your current items: ")
                           print_items()
                           which_item = input("Which item?")
                           if has_item(which_item) == True:
                                for i, value in enumerate(dic_item[key]):
                                    if value == which_item:
                                        del dic_item[key][i]
                                    
                            
                                if(which_item == "Magnifying Glass"):
                                     peeked = magnifier(count)
                                     print("You've selected the Magnifying Glass!")
                                     print(f"Seems like the next bullet is: {peeked}")
                                     print("Here are the current players and their lives: ")
                                     print_player_lives()
                                     player_to_shoot = input("Now who do you want to shoot? (type your own name if you want to shoot yourself)")
                                     if(current_bullet == "live"):
                                        name_lives[player_to_shoot] -= 1
                                        print("Bam, you hit!")
                                        print("Here are the current players and their lives now: ")
                                        print_player_lives()
                                     else:
                                          print("Seems like it was a miss")
                                     
                                if(which_item == "Saw"):
                                     print("You've selected a saw!")
                                     print("Here are the current players and their lives: ")
                                     print_player_lives()
                                     player_to_shoot = input("Now who do you want to shoot? (type your own name if you want to shoot yourself)")
                                     if(current_bullet == "live"):
                                        saw(player_to_shoot) #if current bullet is live, then use saw on selected person
                                        print("Bam, you hit!")
                                        print("Here are the current players and their lives now: ")
                                        print_player_lives()
                                     else:
                                          print("Seems like it was a miss")
                                if(which_item == "Handcuffs"):
                                      print("You've selected some nice shiny cuffs!")
                                      global player_lose_turn
                                      global lost
                                      lost = False #to keep track if player has already skipper turn
                                      player_lose_turn = handcuffs()
                                      print(f"Well I suppose {player_lose_turn} will be skipping their turn next")
                                      print("Here are the current players and their lives: ")
                                      print_player_lives()
                                      player_to_shoot = input("Now who do you want to shoot? (type your own name if you want to shoot yourself)")
                                      if(current_bullet == "live"):
                                             print("Bam, you hit!")
                                             print("Here are the current players and their lives now: ")
                                             print_player_lives()
                                      else:
                                             print("Seems like it was a miss")
                                
                                count+=1
                                print(f"The current count is now: {count}")
                                cleared = clear_player() # clear any players that have 0 lives left
                                if cleared == True:
                                     num_players-=1
                                print(f"The current number of players is: {num_players}")
                                if num_players < 2:
                                    defeat = True
                                    break
                
                                if(count >= num_bullet): #if the count becomes more than the num_bullets, break out of loop and round is over
                                    print("Seems that the racks are empty")
                                    empty = True
                                    break

                      if empty == True or defeat == True:
                        break
                 if empty == True or defeat == True:
                    break
            if defeat == True or empty == True:
                break
        if defeat == True:
                break
                      
                      
    
if __name__ == "__main__":
    main()
            
         
    








