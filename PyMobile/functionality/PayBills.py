import classes.Bill_Payments
import classes.Options
from database.Bills_db import paybill_fetchtable,get_bal,set_bal_bill,delete_row,set_bal_Bank
def payBills(User_ID):
    print('Your existing billers:')
    list_pay=paybill_fetchtable(User_ID)
    choice2=input('--Press any other key for Back--\nChoose the biller: ')
    if(choice2.isdigit() and int(choice2)<=len(list_pay)):
        print(list_pay[int(choice2)-1])
        print('Your current balance is: '+str(get_bal(User_ID)))
        amount=int(input('Enter amount you want to pay: '))
        if (amount<=get_bal(User_ID)):
            choice3=input('Confirm(Y/N): ')
            if(choice3.upper()=='Y'):
                try:
                    if(amount==int((list_pay[int(choice2)-1])[2])):
                        delete_row(User_ID,(list_pay[int(choice2)-1])[0],amount)
                    elif(amount<int((list_pay[int(choice2)-1])[2])):
                        set_bal_bill(User_ID,(list_pay[int(choice2)-1])[0],amount)
                    else:
                        print('Excess Payment. Cancelling Transaction')
                        payBills(User_ID)
                    set_bal_Bank(User_ID,amount)
                    print('Payment Successful....')
                    print('Your current balance is: '+str(get_bal(User_ID)))
                except:
                    print('Payment Unsuccessful....')
                    print('Your current balance is: '+str(get_bal(User_ID)))
            else:
                print('Operation Cancelled')
                print('Your current balance is: '+str(get_bal(User_ID)))
            payBills(User_ID)
        else:
            choice4=input('Insufficient Fund....Do you want to continue(Y/N): ')
            if(choice4.upper()=='Y'):
                payBills(User_ID)
            else:
                classes.Options.options()
    else:
        print('Operation Cancelled')
        classes.Bill_Payments.Bill_Payments()