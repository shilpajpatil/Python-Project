#-------------------rock paper scissors game--------------------------------------
"""
project name:RockPaperScissorsGame.py
purpose: Creating a  game to play with computer
Author: Shilpajpatil

"""
import random
#----------------------main fun---------------
def main():
    comp_wins = 0
    player_win = 0
    while True:
        print("---------")
        user_choice=chose_option()                                                                 #function call with no parameters
        comp_choice=computer_choice()                                                              #function call with no parameters
        print("------------")
  
         if user_choice == "r":                                                                   
            if comp_choice =="r":
                print("you choose rock. computer chose rock.   you Tied.")
            elif comp_choice == "p":
                print("you choose rock.  computer chose paper.  you lose.")
                comp_wins +=1
            elif comp_choice == "s":
                print("you choose rock.   computer chose scissor. you Win. ")
                player_win +=1
        elif user_choice =="p":
            if comp_choice =="r":
                print("you choose paper. computer chose rock.   you win.")
                player_win +=1
            elif comp_choice == "p":
                print("you choose paper. computer chose paper.   you Tied.")
            elif comp_choice == "s":
                print("you choose paper. computer chose rock.   you lose.")
                comp_wins +=1

        elif user_choice=="s":
            if comp_choice == "r":
                print("you choose scissor. computer chose rock.   you lose.")
                comp_wins +=1
            elif comp_choice == "p":
                print("you choose scissor. computer chose paper.   you win.")
                user_choice +=1
            elif comp_choice =="s":
                print("you choose scissor. computer chose scissor.   you Tied.")


        print("-----------------------------")
        print("player wins:",player_win)
        print("computer wins:",comp_wins)

        user_choice=input("Do ou want to play again?(y/n)")                                                             
        if user_choice in ["Y","y","yes","Yes"]:
            pass
        elif user_choice in ["N","n","no","No"]:
            break
        else:
            break




def chose_option():
    user_choice=input("select rock,paper,scissor");
    if user_choice in ["rock","Rock","R","r"]:
        user_choice="r"
    elif user_choice in ["paper","Paper","P","p"]:
        user_choice="p"
    elif user_choice in ["scissor,Scissor","S","s"]:
        user_choice="s"
    else:
        print("Plese choose correct option")
        chose_option()
    return user_choice;


def computer_choice():
    comp_choice=random.randint(1,3)
    if comp_choice==1:
        comp_choice="r"
    elif comp_choice==2:
        comp_choice="p"
    else:
        comp_choice="s"
    return comp_choice;


#if __name__ =="__main__":
main()
