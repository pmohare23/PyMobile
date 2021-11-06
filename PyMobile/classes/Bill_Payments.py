import functionality.PayBills
import functionality.AddBillers
import classes.Log_in
import classes.Options
class Bill_Payments:
    def __init__(self):
        User_ID=classes.Log_in.Login.User_ID
        choice=input('Hi '+User_ID+'...\nWhat do you want to do?\n1. Pay Bills\n2. Add Billers\n--Press any other key for Back--\n')
        if(choice=='1'):
            functionality.PayBills.payBills(User_ID)
        elif(choice=='2'):
            functionality.AddBillers.addBillers(User_ID)
        else:
            classes.Options.options()