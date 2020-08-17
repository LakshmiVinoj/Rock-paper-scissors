from random import randint

# global variables
choices = ["r", "p", "s"]
comp_play = choices[randint(0,2)]
#***********************************************************************************************************************

# user inputs
player_name = input("enter player name: ")
#***********************************************************************************************************************

# keys
print("r -> rock\np -> paper\ns -> scissors")
#***********************************************************************************************************************

# rock paper scissor working 
def game():
    rounds = int(input("enter no of rounds: "))
    comp_score = 0
    player_score = 0   
    for i in range(0, rounds):
        user_choice = input("your choice: ") 
        if user_choice == comp_play:
            print("tie")
    
        elif user_choice == "r":
            if comp_play == "s":
                player_score+=1
                print("u won")
            else:
                comp_score+=1
                print("u lost") 
                
        elif user_choice == "p":
            if comp_play == "r":
                player_score+=1
                print("u won")
            else:
                comp_score+=1
                print("u lost")        
        else:
            if comp_play == "r":
                player_score+=1
                print("u won")
            else:
                comp_score+=1
                print("u lost")  
                
        # score display
        print("+"+ "-"*(len(player_name) + 13) + "+")
        print("| computer | "+ player_name + " |")
        print("|"+("-" * (len(player_name) + 13))+ "|")
        print("| " + str(comp_score) +(" " * 8)+"| "+ str(player_score) +(" " *(len(player_name)-1))+" |")
        print("+"+ "-"*(len(player_name) + 13) + "+")   
    
    # finds winner 
    def winner():
        if player_score > comp_score:
            print("The winner is " + player_name)
        elif player_score < comp_score:
            print("The winner is computer") 
        else:
            print("It is a tie")
            
    winner()
        
    n = int(input("rematch?\nyes -> 1\nno -> 0\nenter: "))
    if n==1:
        game()
    
#***********************************************************************************************************************

game()
