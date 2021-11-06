from functionality.new_account import new_account
def account_summary(list_accounts):           
    option=input("Do you wish to view any account summary?(Y/N): ")
    if option=="Y" or option=="y":
        option1=input("Which account do you want to view?: ")
        if option1.isdigit():                
            if(int(option1)<=len(list_accounts)):
                hold=list_accounts[int(option1)-1]
                print("Account Holder Name:"+str(hold[2])+"\nAccount Type:"+str(hold[1])+"\nAccount Number:"+str(hold[0])+"\nAccount Balance:"+str(hold[3]))
                new_account()
            else:
                print("Account does not exists,try again")
                account_summary(list_accounts)
        else:
            print("Enter Valid Choice: ")
            account_summary(list_accounts)
    elif(option=="N"or option=="n"):
        new_account()
    else:
        print("Enter Valid Choice: ")
        account_summary(list_accounts)