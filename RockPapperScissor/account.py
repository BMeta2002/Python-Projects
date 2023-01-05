import subprocess
print ("------------------------------------")
print("Rock, Paper, Scissors Account Setup")
print ("------------------------------------")
while True:
  username = input("Pick a Username:  ")
  password = input("Pick a Password:  ")
  password_confirm = input("Please confirm your password: ")

  if password != password_confirm:
    print("Your passwords dont match, Please try again.")

  if password == password_confirm:
    print("Your Account has been set up, Enjoy The Game! ")
    text_file = open("accounts.csv" , "a")
    text_file.write(",")
    text_file.write(username)
    text_file.write(",")
    text_file.write(password_confirm)
    text_file.close()
    break
    subprocess.call(["python", "main.py"])
    
  