import re
import sys
from log_with_openpyxl import logging_transaction, output_user_specific_transactions

account_details = {
  'dun1':{
    'Name': 'Duncan',
    'Username' : 'duncmaster',
    'Password' : 'DuncanLikesCoding123',
    'Initial deposit' : 300,
    'Account balance' : 300,
  },
  'vic2':{
     'Name': 'Vico',
     'Username' : 'redvjs',
     'Password' : 'NetherlandsW1llW1n',
     'Initial deposit' : 5,
     'Account balance' : 5,
  },
  'wil3':{
     'Name': 'Wilson',
     'Username' : 'wilsonistheman',
     'Password' : '1WilsonAndADream',
     'Initial deposit' : 250,
     'Account balance' : 250,
  },

}

# Main, calls starting function login_menu
def main():
    start_menu()

# Output login menu options.
# executes correct function based on input selection using valid_selection function.
def start_menu():
  print("\nWelcome to Mega-Bank, how would you like to proceed?\n")
  print("1. Open a new account")
  print("2. Login in to an existing account")
  print("3. Exit\n")
  
  menu_choice = valid_selection("Please enter your choice (1, 2, 3): ", 3)
  match menu_choice:
    case 1:
        account_creation()
    case 2:
        login_flow()
    case 3:
        sys.exit("Goodbye!")

def get_login_details():
    print("\n--- Please enter your login details --- \n")
    unique_id = get_user_unique_id()
    username = input("Please enter your username: ").lower().strip()
    password = input("Please enter your password: ")
    return unique_id, username, password

def validate_login(unique_id, username, password):
    username_match = re.fullmatch(username, get_user_detail(unique_id, 'username'))
    password_match = re.fullmatch(password, get_user_detail(unique_id, 'password'))
    return username_match is not None and password_match is not None

# Checks whether input details match stored details.
# if details match, start main_menu function, passing unique_id to ensure only details related to the logged in user are shown.
def login():
    unique_id, username, password = get_login_details()
    if validate_login(unique_id, username, password):
        print("Login successful!\n")
        return unique_id
    return None

def login_flow():
    n = 3
    while(n >= 1):
        unique_id = login()
        if unique_id:
            return (main_menu_flow(unique_id))
        else:
            print('Login Failed.')
            n -= 1
            print(f'{n} attempts left.')
    return start_menu()
        
        

def main_menu_flow(unique_id):
    if unique_id:
        main_menu(unique_id)

       

# Displays main menu options and executes appropriate function based on input.
def main_menu(current_user):
    user = get_user_detail(current_user, 'name')
    print(f"Welcome {user}")
    print("1. View account summary")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. logout and exit\n")
    
    user_selection = valid_selection("Menu Selection: ", 4)
            
    match user_selection:
        case 1:
            account_summary(current_user)
        case 2:
            deposit(current_user)
        case 3:
            withdraw(current_user)
        case 4:
            exit_or_continue(current_user)

# Account creation function, which takes in users name, then uses the valid_username() and valid_password() functions described below to validate input.
# While loop to validate integer entered correctly.
# confirms if details correct.
# IF details correct and unique_id not in dictionary, IF true appends user details to the end of the dictionary.
def account_creation(): 
  correct_details = False
  while correct_details != True:
    name = input("Please enter your name: ").lower().strip()
    username = valid_username()
    password = valid_password()
    while True:
      try:
        initial_deposit = float(input("Please enter your initial deposit: "))
        break
      except ValueError:
        print("The number you entered is invalid, please try again")
        continue
    unique_id = name[0:3].lower() + str(len(account_details)+1)
    print("You have entered the following details:")
    print(f"Name: {name}")
    print(f'Username: {username}')
    print(f"Initial deposit: £{initial_deposit}")
    confirmation = valid_selection("Is this correct?\n1. Yes\n2. No\n", 2)
    if confirmation == 1:
      print("Account created successfully")
      print(f"Your Unique ID is:{unique_id}")
      correct_details = True
      if (correct_details == True and unique_id not in account_details):
            account_details[unique_id] = {"Name" : name.capitalize(), 'Username' : username, 'Password' : password, 'Initial deposit' : initial_deposit, 'Account balance' : initial_deposit}
            login()
    else:
      print("Please try again.")

# contains regular expression pattern for valid password requirements.
# While loop to check if the password is valid by matching against the RE pattern.
# password_re_entry allows the password to be entered twice to make sure the user has not made a typo when putting in the password the first time.
# Returns password.    
def valid_password():
   valid_password_pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$"
   while True:
    print("Password must be at least eight characters long, contain at least one uppercase letter, at least one lowercase letter, and at least one digit\n")
    password = input("Please enter a password: ")
    password_re_entry = input("Please enter your password again: ")
    if password == password_re_entry:
        match_password = re.match(valid_password_pattern, password)
        if match_password != None:
          print("Password set successfuly")
          return password
        else:
          print("Password does not meet the requirements, please try again.")
          continue
    else:
       print("Passwords dont match, please try again.")

# contains regular expression pattern for valid username requirements.
# While loop to check if the username is valid by matching against the RE pattern.
# Returns username.   
def valid_username():
   valid_username_pattern = r"^(?=.{4,32}$)[a-zA-Z0-9]+$"
   while True:
      username = input("Please enter a username: ").lower().strip()
      match_username = re.match(valid_username_pattern, username)
      if match_username != None:
         return username
      else:
         print("Username must be 4-32 characters long\nUsername can't unclude the following characters ('_, -, .'), please try again.")
         continue

# Returns user details, requires two conditional arguments: unique_id, detail_name. 
# detail_name can be one of the following: 'name', 'username', 'password', 'account_balance'. Default case outputs a message.   
def get_user_detail(unique_id,detail_name):
  match detail_name:
     case 'name':
        return account_details[unique_id]['Name']
     case 'username':
        return account_details[unique_id]['Username']
     case 'password':
        return account_details[unique_id]['Password']
     case 'account_balance':
        return account_details[unique_id]['Account balance']
     case _:
        print("There was a problem retrieving account details.")
  
# Checks if user id is present in account_details dictionary.
# returns unique_id from user input.
def get_user_unique_id():
   while True:
    unique_id = input("Please enter your unique id: ").lower().strip()
    if unique_id in account_details:
        return unique_id
    else:
        print(f"Unique id: {unique_id} not found, please try again.")
        continue

# Allows user to continue back to main menu, or exit/logout.
def exit_or_continue(unique_id):
    user_selection = input("Press enter to continue to main menu, or type 'exit' to exit and logout: ").lower().strip()
    if user_selection == "exit":
        sys.exit("Successfully logged out, thank you for using MegaBank!")
    else:
       main_menu(unique_id)

# Outputs account details for specified user, password is hidden.
# Requires unique_id to be passed in.
def account_summary(current_user):
    name = get_user_detail(current_user, 'name')
    username = account_details[current_user]['Username']
    password = (len(account_details[current_user]['Password'])* '*')
    account_balance = account_details[current_user]['Account balance']
    print(f"---- Account summary for {name} ---")
    print(f"Name: {name}")
    print(f"Username: {username}")
    print(f"Password: {password}")
    print(f"Account balance: {account_balance}")
    transaction_history = valid_selection("Would you like to view your transaction history?\n1. Yes\n2. No\n", 2)
    if transaction_history == 1:
       output_user_specific_transactions(current_user)
    exit_or_continue(current_user)

# deposit function, does not return a value, does not take a value. Currently uses global variable account balance (Which should be changed for security reasons).
# works by asking for float input 'amount_to_deposit'. This amount is added to 'account_balance'.
# catches ValueErrors to ensure valid number is inputted.
# print updated account balance.
# logs the transaction to xl spreadsheet.
def deposit(unique_id):
    account_balance = account_details[unique_id]['Account balance']
    while True:
        try:
            amount_to_deposit = float(input("How much would you like to deposit?: ").strip("-").strip("+"))
            account_balance += amount_to_deposit
            account_details[unique_id]['Account balance'] = account_balance
            print(f"Your new account balance is ${account_details[unique_id]['Account balance']:.2f}")
            break
        except ValueError:
            print("That was an invalid number")
            continue
    logging_transaction(unique_id, "Deposit", amount_to_deposit)
    exit_or_continue(unique_id)
    
# withdraw function, does not return a value, does not take a value. Currently uses global variable account balance (Which should be changed for security reasons).
# Works by asking for float input 'amount_to_withdraw'. This amount is subtracted from 'account_balance' only IF the amount to withdraw is not more than account balance.
# catches ValueErrors to ensure valid number is inputted.
# if amount exceeds account balance, output formatted string to tell user, they will be asked to enter a new amount.
# print updated account balance.
# logs the transaction to xl spreadsheet.
def withdraw(unique_id):
    account_balance = account_details[unique_id]['Account balance']
    while True:
        try:
            amount_to_withdraw = float(input("How much would you like to withdraw?: ").strip("-").strip("+"))
            if(account_balance - amount_to_withdraw >= 0):
                account_balance -= amount_to_withdraw
                account_details[unique_id]['Account balance'] = account_balance
                print(f"Your new account balance is ${account_details[unique_id]['Account balance']:.2f}")
                break
            else:
                print(f"The amount ${amount_to_withdraw:.2f} exceeds the balance of the account: Account balance = ${account_balance:.2f}")
        except ValueError:
            print("That was an invalid number.")
            continue
    logging_transaction(unique_id, 'Withdraw', amount_to_withdraw)
    exit_or_continue(unique_id)

# requires two conditional arguments, the input question, and the max range (Must be an integer between 1-max_range).
# Checks if the user entered a valid integer, raises Value error if not an integer.  
def valid_selection(question, max_range):
    while True:
        try:
            user_selection = int(input(question))
        except ValueError:
            print("You must enter a valid number.")
        else:
            if 1 <= user_selection <= max_range:
                return user_selection
            else:
                print("You entered too many numbers!")


if __name__ == "__main__":
   main()
