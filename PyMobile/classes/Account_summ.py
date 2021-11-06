import functionality.account_summary
import classes.Log_in
from database.Accounts_db import fetch_accounts
class Accounts_and_deposits:
    def __init__(self):
        print('Hi '+classes.Log_in.Login.User_ID+'...\nYour account details are as follows:')
        list_accounts=fetch_accounts(classes.Log_in.Login.User_ID)
        functionality.account_summary.account_summary(list_accounts)