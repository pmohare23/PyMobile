from database.Bills_db import bill_add,verify,bill_fetchtable,bill_update
import classes.Bill_Payments
def addBillers(User_ID):
        choice5=input('Account Number: ')
        choice6=input('Account Name: ')
        choice7=input('Type of Biller (Credit Card/Debit Card/Cash): ')
        choice8=input('Amount: ')
        if(choice5.isdigit() and verify(choice5,choice6) and choice7 in ('Credit Card','Debit Card','Cash')):
            if(choice8.isdigit()):
                choice9=input('Confirm(Y/N): ')
                if(choice9.upper()=='Y'):
                    list_pay=bill_fetchtable(User_ID)
                    if(choice5 in list_pay):
                        bill_update(User_ID,choice5,choice8)
                    else:
                        bill_add(User_ID,choice5,choice8,choice7)
                    print('Biller added successfully')
                    classes.Bill_Payments.Bill_Payments()
                else:
                    print('Operation Cancelled')
                    classes.Bill_Payments.Bill_Payments()
            else:
                print('Incorrect Amount')
                addBillers(User_ID)
        else:
            print('Incorrect data, Operation Terminated')
            classes.Bill_Payments.Bill_Payments()