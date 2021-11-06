import classes.Bill_Payments
import classes.Account_summ
import classes.Fund_Transfer
import classes.ViewT
import utility.Menu
count=0
def options():
    global count
    if(count<3):
        user_option=input("Main Menu\n----------\n1. Fund Transfer\n2. Accounts and Deposit \n3. Bill Payments\n4. View Recent transactions\n5. Log Out\nChoose an option: ")
        if(user_option=='1'):
            count=0
            classes.Fund_Transfer.Fund_Transfer()
        elif(user_option=='2'):
            count=0
            classes.Account_summ.Accounts_and_deposits()
        elif(user_option=='3'):
            count=0
            classes.Bill_Payments.Bill_Payments()
        elif(user_option=='4'):
            count=0
            classes.ViewT.View_Transaction()
        elif(user_option=='5'):
            utility.Menu.Menu()
        else:
            print('Wrong option')
            count+=1
            options()