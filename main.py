from asyncio.windows_events import NULL
import random
import os


def accountInfo(accountNumber):
    with open("accountNum.txt", 'w') as file:
        file.write(accountNumber + "\n")

def cvvInfo(cvvNum):
    with open("cvvNum.txt", 'w') as file:
        file.write(cvvNum)

adminAccount = 123456789012
adminCvv = 123


name = input("\u001b[37;1mHey, Enter your name: ")
print("\n\n\n\n\n\nWelcome, " + name + " in our Obama bank :)\n")

print("\033[1;32mDo you want to login(1) or sign-up(2): ")
inp = int(input())


def accountInfo(email):
    while 1:
        print("\033[;32mHey," + name + ". Your info follow as :-\n")
        print("Your name is " + name)
        print("\u001b[37;1m2. Account number: " + (open("accountNum.txt").read()))
        "accountNum.txt".close()
        print("3. CVV number: " + (open("cvvNum.txt").read()))
        "cvvNum.txt".close()
        print("4. Your email id is: " + email)
        ainp1 = int(input("\n\n5. to back press '9'\n6. To quit press '0': \n"))

        if ainp1 == 0 and ainp1 != 9:
            ending()
            break
        elif ainp1 == 9 and ainp1 != 0:
            economy()
            break
        else:
            print("Enter valid input")
        


#Economy part
def economy():
    while 1:
        ecoinp = int(input("""
        Select any of the following:-
            1. Account Info 
            2. Balance
            3. Withdraw
            4. Deposit
            5. Close this account
            6. Help Menu
            
            0. Exit
        """))

        if ecoinp == 0:
            ending()
            break

        elif ecoinp == 1:
            accountInfo()
            break

        elif ecoinp == 5:
            with open("accountNum.txt", 'w') as file:
                file.write("")
            with open("cvvNum.txt", 'w') as file:
                file.write("")
        elif ecoinp == 6:
            print("Help Menu has been sended to your email.")
        elif ecoinp == 2:
            print("") #need to do this after eco system
        elif ecoinp == 3:
            print("")
        elif ecoinp == 4:
            print("")


#signup part
def signup():
    while 1:
                email = input("\u001b[37;1mEnter you email id: ")
                if(email[-10:] != "@gmail.com"):
                    print("\033[31;1mPlease enter valid email id.")
                    continue
                else:
                    emPassword = input("Enter your emergency password (Must having 12 letters): ")
                    if emPassword == NULL or len(emPassword) < 12:
                        print("\033[31;1mWTF! We already said that password should contain atleast 12 letters.")
                        continue
                    else:
                        break

#ENDing here not at the end of program
def ending():
    print("\n\n\n\n\n\n\n \u001b[0mSad life that you are going! Remember now we will use your money to buy some boom boom :) (T&A apply)")


#LOGIN Part

def login():
    while 1:
        print("\n\n\n\n\n\n\u001b[35mLOGIN\n\n")
        inAccountNumber = int(input("\u001b[37;1mEnter your account number | '0' for exit: "))
        if inAccountNumber == adminAccount and inAccountNumber != 0:
            print("Welcome back admin") #Need to do this after economy part and other stuffs
        elif inAccountNumber == int((open("accountNum.txt").read())) and inAccountNumber != 0:
            inCvvNum = int(input("Enter your cvv (You can find it back of your card): "))
            if inCvvNum == int(open("cvvNum.txt").read()):
                print("\033[1;32m\n\n\n\n\n\n\nWelcome back " + name + ". You have logged in successfully")
                economy()
            break
        elif inAccountNumber != accountNumber and inAccountNumber != 0:
            print("\033[31;1mWrong account number")
            continue
        elif inAccountNumber == 0:
            ending()
            break

        else:
            print("\033[31;1mWrong input!")
            continue
        


while 1:
    if inp == 1:
        login()
        break
    
        
    if inp == 2:
        print("\n\n\n\n\n\n\u001b[35mSIGN-UP\n\n")
        inp2 = input("\u001b[37;1mYour name is " + name + "? ('y'ES/'n'O): ")
        while 1:
            if inp2 == 'y' or inp2 == 'Y':
                signup()
                break
            elif inp2 == 'n' or inp2 == 'N':
                name = input("Enter you name: ")
                signup()
                break
            else:
                print("\033[31;1mWrong input! try again.\n\n\n\n")
        accountNumber = random.randint(100000000000,999999999999)
        accountInfo(str(accountNumber))
        cvvNum = random.randint(111,999)
        cvvInfo(str(cvvNum))
        print("\n\n\n\n\n\n\n\n\u001b[37;1mYour Account number is: " + str(accountNumber))
        print("\nYour Account cvv is: " + str(cvvNum))

        inp3 = int(input("\u001b[35mPress '1' to continue '0' to exit: "))
        if inp3 == 1:
            inp = 1
        elif inp3 == 0:
            ending()
            break
        else:
            print("Wrong input!")

    else:
        print("\033[31;1mWrong input! Choose again")
        inp = int(input("\033[1;32mPlease choose correct input! login(1) or sign-up(2): "))


