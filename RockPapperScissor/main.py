# Get ready to have some fun!!!
import random
import time
import subprocess

print(
  "-----------------------------Verison 2.0--------------------------------")
print(
  "Made by Bilal Malik. Visit https://github.com/BMeta2002 to check me out!")
print(
  "************************************************************************")

lose = ("Really Lost To A Computer Geez :)")
win = (
  "Bilal Is Proud Of You For Beating The Computer Now Go Study JavaScript")
lives = 5
score = 0
draw = 0
computer_lives = 7

while True:
  print("To begin in the below information.")
  username = input("Please enter your username:    ")
  password = input("Please enter your password:    ")
  search_file = open("accounts.csv", "r")
  for line in search_file:

    if username and password in line:
      print("Access Granted")
      time.sleep(0.5)
      print("Loading.....")
      time.sleep(0.5)
      print("Loading.....")
      time.sleep(0.5)
      print("Loading.....")
      time.sleep(0.5)
      print("Loading.....")
      time.sleep(0.5)
      print("Almost there.....")
      time.sleep(0.5)
      print("Last One Promise...")
      time.sleep(0.5)
      print("Really The Last one....")
      time.sleep(2.0)
      print("""
                          .______        ______     ______  __  ___ 
                          |   _  \      /  __  \   /      ||  |/  / 
                          |  |_)  |    |  |  |  | |  ,----'|  '  /  
                          |      /     |  |  |  | |  |     |    <   
                          |  |\  \----.|  `--'  | |  `----.|  .  \  
                          | _| `._____| \______/   \______||__|\__\    
      """)
      time.sleep(0.5)
      print("""
                      .______      ___      .______    _______ .______      
                      |   _  \    /   \     |   _  \  |   ____||   _  \     
                      |  |_)  |  /  ^  \    |  |_)  | |  |__   |  |_)  |    
                      |   ___/  /  /_\  \   |   ___/  |   __|  |      /     
                      |  |     /  _____  \  |  |      |  |____ |  |\  \----.
                      | _|    /__/     \__\ | _|      |_______|| _| `._____|
      """)
      time.sleep(0.5)
      print("""
               _______.  ______  __       _______.     _______.  ______   .______      
              /       | /      ||  |     /       |    /       | /  __  \  |   _  \     
             |   (----`|  ,----'|  |    |   (----`   |   (----`|  |  |  | |  |_)  |    
              \   \    |  |     |  |     \   \        \   \    |  |  |  | |      /     
          .----)   |   |  `----.|  | .----)   |   .----)   |   |  `--'  | |  |\  \----.
          |_______/     \______||__| |_______/    |_______/     \______/  | _| `._____|

      """)
      time.sleep(0.5)
      print("-------------------------------------")
      print(f"You start with {lives} lives")
      print("If you lose you lose a live")
      print("if you draw the lives stay the same")
      print("-------------------------------------------------- \n")
      print("------To see a list of rules type rules-----------")
      print("-------------------------------------------------- \n")
      print("------To see a list of commands type commands-----")
      print("--------------------------------------------------")
      print("The computer had lives as well")
      print("Can You Beat The Brainiac ?")
      print("Good Luck Have Fun! \n")
      while True:
        print("Enter Your Weapon Of Choice")
        user = input("Rock, Paper, Scissors?    \n")
        user = user.title()
        computer = ("rock", "paper", "scissors")
        computer = random.choice(computer)

        #Rock If Statement
        if user == "Rock" and computer == "paper":
          print("--------------------------------------")
          print(f"The computer choose {computer}")
          print("--------------------------------------")
          print(lose)
          print("--------------------------------------")
          lives -= 1
        if user == "Rock" and computer == "scissors":
          print("--------------------------------------")
          print(f"The computer choose {computer}")
          print("--------------------------------------")
          print(win)
          print("--------------------------------------")
          score += 1

        #paper If Statement
        if user == "Paper" and computer == "rock":
          print("--------------------------------------")
          print(f"The computer choose {computer}")
          print("--------------------------------------")
          print(win)
          computer_lives -= 1
          print("--------------------------------------")
          score += 1
        if user == "Paper" and computer == "scissors":
          print("--------------------------------------")
          print(f"The computer choose {computer}")
          print("--------------------------------------")
          print(lose)
          print("--------------------------------------")
          lives -= 1

        #Scissor If Statement
        if user == "Scissors" and computer == "paper":
          print("--------------------------------------")
          print(f"The computer choose {computer}")
          print("--------------------------------------")
          print(win)
          computer_lives -= 1
          print("--------------------------------------")
          lives += 1
        if user == "Scissors" and computer == "rock":
          print("--------------------------------------")
          print(f"The computer choose {computer}")
          print("--------------------------------------")
          print(win)
          print("--------------------------------------")
          score += 1

          #Duplicates(Tied)
        if user == "Rock" and computer == "rock":
          print("--------------------------------------")
          print(f"The computer choose {computer}")
          print("--------------------------------------")
          print("You Tied")
          print("--------------------------------------")
          draw += 1

        if user == "Paper" and computer == "paper":
          print("--------------------------------------")
          print(f"The computer choose {computer}")
          print("--------------------------------------")
          print("You Tied")
          print("--------------------------------------")
          draw += 1

        if user == "Scissors" and computer == "scissors":
          print("--------------------------------------")
          print(f"The computer choose {computer}")
          print("--------------------------------------")
          print("You Tied")
          print("--------------------------------------")
          draw += 1

        #System
        if user == "Rules":
          print("**************************************")
          print("-------------Rules--------------------")
          print("**************************************")
          print("Rock loses against Paper")
          print("Rock beats Scissors")
          print("Paper beats Rock")
          print("Paper loses against Scissors")
          print("Scissors beats Paper")
          print("Scissors loses against Rock")
          print("**************************************")

        if user == "Commands":
          print("**************************************")
          print("------------Commands------------------")
          print("**************************************")
          print("Type Lives To See The amount of Lives you have left")
          print("Type Score To See If Your Winning")
          print("Type Draw To See How Many Times You Have Tied")
          print("**************************************")

        if user == "Lives":
          print("--------------------------------------")
          print(f"You have {lives} left ")
          print("--------------------------------------")
        if user == "Score":
          print("--------------------------------------")
          print(f"Your Score Is {score}")
          print("--------------------------------------")
        if user == "Draw":
          print("--------------------------------------")
          print(f"You have tied {draw} times")
          print("--------------------------------------")

        # Lives
        if lives == 0 or user == "Test":
          print("--------------------------------------")
          print("Thanks for playing")
          print("You have ran out of lives")
          print("--------------------------------------")
          print(f"You got {score} correct")
          print(f"You tied {draw} times")
          print("--------------------------------------")
          stop = input("Press enter to exit")
          exit()

        if computer_lives == 0:
          print("--------------------------------------")
          print("Thanks for playing")
          print("The computer lost all it's lives you win")
          print("--------------------------------------")
          print(f"You got {score} correct")
          print(f"You tied {draw} times")
          print("--------------------------------------")
          stop = input("Press enter to exit")
          exit()

          #exit
          if user == "Exit":
            break
  else:
    print("Your Username Or Password is incorrect")
    print("---------------------------------------")
    subprocess.call(["python", "account.py"])
