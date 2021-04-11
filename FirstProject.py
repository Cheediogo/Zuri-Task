import random

database = {}   

def init():

    print("Welcome to Saphire Bank!")

    haveAccount = int(input("Do you have an account with us? 1 (yes) 2 (no) \n" ))

    if(haveAccount == 1):
         
        login()
    elif(haveAccount == 2):
           
        register()
    else:
        print("You have selected an invalid option")
        init()    

def login():
    print("******** Login ********")

    accountNumberFromUser = int(input("What is your account number?\n"))
    password = input("What is your password?\n")

    for accountNumber, userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(password == userDetails[3]):
                welcome(userDetails)
                
    print("Invalid account or password")
    login()
    

def register():

    print("********* Register *********")

    email = input("What is your email address? \n")
    firstName = input("What is your first name? \n")
    lastName = input("What is your last name? \n")
    password = input("Create your password \n")

    accountNumber = generateAccountNumber()

    database[accountNumber] = [ firstName, lastName, email, password ]

    print("Your account has been created")
    print(" === ==== ====== ===== ===")
    print("Your account number is: %d" % accountNumber)
    print("Do not share your login details with anyone")
    print(" === ==== ====== ===== ===")

    login()


def welcome(user):
    print("Welcome %s %s " % ( user[0], user[1] ) ) 
    bankOperation()

def bankOperation():
    selectedOption = int(input("What would you like to do? (1) deposit (2) withdrawal (3) check balance (4) logout (5) exit\n"))

    if(selectedOption == 1):
        depositOperation()
               
    elif(selectedOption == 2):
        withdrawalOperation()

    elif(selectedOption == 3):
        balanceOperation()

    elif(selectedOption == 4):
        logout()

    elif(selectedOption == 5):
        exit()

    else:
        print("Invalid option selected")  
        bankOperation()  

def depositOperation():
    creditAmount = int(input("How much would you like to Deposit?\n"))
        
    if(creditAmount >= 100):
        print('Transaction successful')
        print("Thanks for choosing Saphire Bank!")
        exit()
    else:
        print("You can only deposit NGN100 and above")
        anotherTransaction = int(input("Would you like to perform another transaction? (1) Yes (2) No\n"))
        if(anotherTransaction == 1):
            bankOperation()
        
        else:
            print("Thanks for choosing Saphire Bank!")
            exit()

def withdrawalOperation():
    debitAmount = int(input("How much would you like to withdraw?\n"))
    print("Take your cash")
    print("Thanks for choosing Saphire Bank!")
    exit()

def balanceOperation():
    print("See your current balance below")
    anotherTransaction = int(input("Would you like to perform another transaction? (1) Yes (2) No\n"))
    if(anotherTransaction == 1):
        bankOperation()   
    else:
        print("Thanks for choosing Saphire Bank!")
        exit()

def generateAccountNumber():

    return random.randrange(1111111111,9999999999)

def logout():
    login()

  

init()