# MegaBank
    #### Video Demo:  https://youtu.be/Dtfr5KOkKmU
    #### Description:
        a simple command-line banking system. This application allows users to create accounts, log in, view account summaries and transaction history, make deposits, and withdraw funds. The openpyxl library is used to log transactions using datetime to include a timestamp, and the termcolor library is used to format the retrieved excel spreadsheet values. 

    Features:

        Account Creation: Users can create new accounts with unique usernames and secure passwords.
        Login System: Users can log in to their accounts using their unique ID, username, and password.
        Account Summary: Users can view their account details and balance.
        Deposit: Users can deposit funds into their accounts.
        Withdraw: Users can withdraw funds from their accounts.
        Transaction Logging: All transactions are logged and can be reviewed by the user.
        Extensions and Future Improvements:

    Functionality Enhancements:
            -Password protection: Add password protection for user accounts to enhance security. Ensure passwords are hashed before storing them.
            - Admin Mode: Implement an admin mode to allow administrators to view and manage all user accounts, which can be useful for maintaining the system.
            - Interest Calculations and Transfers: Add features like interest calculations for savings and the ability to transfer money between accounts to make the system more comprehensive.
            - Implement database to push and pull user details from

    Prerequisites:

        Python 3.x
        Required libraries: openpyxl, termcolor, regular expression (RE), datetime
        You can install the required libraries using pip:
            pip install openpyxl termcolor

    Getting Started:

        Clone the repository or download the source code.
        Ensure you have the required libraries installed.
        Run the main script.
        python megabank.py

    Project Structure:

        megabank.py: The main script containing the application logic.
        log_with_openpyxl.py: Module for logging transactions and outputting user-specific transaction histories.
        Usage:

        Main Menu:

            Upon running the application, you will be presented with the main menu:
                Welcome to Mega-Bank, how would you like to proceed?
                1. Open a new account
                2. Login in to an existing account
                3. Exit
    
        Account Creation:

            To create a new account, select option 1. You will be prompted to enter your name, a valid username, a secure password, and an initial deposit. Ensure your username and password meet the specified requirements:
            Username: 4-32 characters long, containing letters, digits, underscores, hyphens, or dots.
            Password: At least eight characters long, containing one uppercase letter, one lowercase letter, and one digit.
    
        Login:

            To log in, select option 2. Enter your unique ID, username, and password. Upon successful login, you will be directed to the main menu.
    
        Main Menu (Post-login):

            After logging in, the following options are available:
                Welcome [Username]
                1. View account summary
                2. Deposit
                3. Withdraw
                4. Logout and exit
        
            View Account Summary:
        
                Select option 1 to view your account summary. You can also choose to view your transaction history.
            
            Deposit:
        
                Select option 2 to deposit funds into your account. Enter the amount you wish to deposit, and your account balance will be updated accordingly.
            
            Withdraw:
        
                Select option 3 to withdraw funds from your account. Ensure you do not withdraw more than your account balance.
            
            Logout and Exit:
        
                Select option 4 to logout and exit the application.

    Helper Functions:

        valid_password(): Ensures password meets security requirements.
        valid_username(): Ensures username meets format requirements.
        get_user_detail(unique_id, detail_name): Retrieves specific user details.
        get_user_unique_id(): Validates the unique ID entered by the user.
        exit_or_continue(unique_id): Allows user to continue or exit after completing an action.
        valid_selection(question, max_range): Validates user menu selections.

    Logging Transactions:

        All transactions are logged using functions from the log_with_openpyxl module:

        logging_transaction(unique_id, type, amount): Logs the time of the transaction, user's unique ID, transaction type, and amount. Saves the details in an Excel spreadsheet.
        output_user_specific_transactions(unique_id): Outputs the transaction history for the specified user, formatting the output into a table with colored headers and transaction types.
        Example Logging Function:

            def logging_transaction(unique_id, type, amount):
                log_file_location = r"C:\Users\Vico Schot\Documents\Software Development Course\Group Banking App\Group Banking App\transaction_log.xlsx"
                log_file = openpyxl.load_workbook(log_file_location)
                current_sheet = log_file.active
                time_stamp = datetime.now()
                time_stamp_string_format = time_stamp.strftime("%m/%d/%Y at %H:%M:%S")
                current_sheet.cell(column=1, row=current_sheet.max_row+1, value=time_stamp_string_format)
                current_sheet.cell(column=2, row=current_sheet.max_row, value=unique_id)
                current_sheet.cell(column=3, row=current_sheet.max_row, value=type)
                current_sheet.cell(column=4, row=current_sheet.max_row, value=amount).number_format= '£0.00'
                log_file.save("transaction_log.xlsx")

        Example Transaction History Function:

            def output_user_specific_transactions(unique_id):
                log_file_location = r"C:\Users\Vico Schot\Documents\Software Development Course\Group Banking App\Group Banking App\transaction_log.xlsx"
                log_file = openpyxl.load_workbook(log_file_location)
                current_sheet = log_file.active
                print(colored("|          Time Stamp          |     Unique ID    |     Transaction Type    |    Amount    |", 'white', attrs=['bold']))
                for row in current_sheet.iter_rows(min_row=2, values_only=True):
                    if row[1] == unique_id:
                        if row[2] == 'Deposit':
                            print(colored(f"|    {row[0]}    |        {row[1]}      |          {row[2]}        |     £{row[3]}     |", "green"))
                        else:
                            print(colored(f"|    {row[0]}    |        {row[1]}      |          {row[2]}       |     £{row[3]}     |", "red"))
                            
License This project is licensed under the MIT License.

Acknowledgments Special thanks to all contributors and the open-source community for their valuable resources and support.