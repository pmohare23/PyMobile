import functionality.account_summary
import classes.Log_in
from database.Accounts_db import fetch_accounts
class Accounts_and_deposits:
    def __init__(self):
        print('Hi '+classes.Log_in.Login.User_ID+'...\nYour account details are as follows:')
        list_accounts=fetch_accounts(classes.Log_in.Login.User_ID)
        functionality.account_summary.account_sumimport classes.Log_in
import classes.Options
from database.View_db import fetch_trans,fetch_accounts
class View_Transaction:
    def __init__(self):
        User_ID=classes.Log_in.Login.User_ID
        print('Hi '+User_ID+'...')
        count=1
        list_acc=fetch_accounts(User_ID)
        for i in list_acc:
            print(str(count)+' Account Number: '+str(i[0])+'-'+i[1])
            count+=1
        print('--Press any other key for back--')
        choice=input('Choose the account: ')
        if(choice.isdigit() and int(choice)<=len(list_acc)):
            accno=(list_acc[int(choice)-1])[0]
            print('Recent Transactions made for Account Number '+str(accno)+':')
            trans=fetch_trans(accno)
            count=1
            for i in trans:
                print(str(count)+' '+i[2]+'/'+i[0]+'/'+str(i[1])+str(int(i[4])%1000000))
            choice2=input('Choose the transaction:' )
            if(choice2.isdigit() and int(choice2)<=len(trans)):
                disp=trans[int(choice2)-1]
                print(disp[0]+'-'+str(disp[4])+'\nAmount Transferred: '+str(disp[3])+'\nDate: '+str(disp[1]))
            else:
                View_Transaction()
        else:
            classes.Options.options()mary(list_accounts)