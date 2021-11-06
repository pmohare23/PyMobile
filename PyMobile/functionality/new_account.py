import classes.Options
import classes.Log_in
import database.Accounts_db
import functionality.Gen_Captcha
import functionality.gen_uid
import validations.Validations
def new_account():        
    option2=input("Do you wish to open a new account?(Y/N): ")
    if option2=="Y" or option2=="y":
        option3=input("Enter the type of account you want to open 1.FD 2.RD: ")     
        if option3.upper()=="FD" or option3=='1' or option3.upper()=="RD"or option3=="2":
            option4=input("enter the amount to be deposited: ")
            if option4.isdigit():
                if int(option4)<=database.Accounts_db.get_balance(classes.Log_in.Login.User_ID):
                    option5=input("Confirm(Y/N): ")
                    if option5=="Y"or option5=="y":
                        if(option3.upper()=="RD"or option3=="2"):
                            option6=input("Enter total no of months: ")
                            if(option6.isdigit() and int(option6)>0):
                                new_detail=database.Accounts_db.acc_details(classes.Log_in.Login.User_ID)
                                mmid=functionality.Gen_Captcha.mmid_gen()
                                uid=functionality.gen_uid.generate_uid(new_detail[0])
                                new_account_no=input("New Account No: ")
                                existing=database.Accounts_db.existing_Account()
                                while new_account_no in existing:
                                    print("Account number already exists,Please try again")
                                    new_account_no=input("New Account No: ")
                                try:
                                    validations.Validations.validate_acct_no(new_account_no)
                                    new_ifsc=functionality.Gen_Captcha.gen_ifsc()
                                    exists=database.Accounts_db.existing_ifsc()
                                    while new_ifsc in exists:
                                        print("IFSC already exists,Please try again")
                                        new_ifsc=input("New IFSC: ")
                                    database.Accounts_db.set_rd_fd(classes.Log_in.Login.User_ID,new_account_no,new_ifsc,uid,'RD',option4,option6,mmid)
                                except:
                                    print('Account Number Invalid')
                                    new_account()
                            else:
                                print('Please enter valid no. of months')
                                new_account()
                        else:
                            new_detail=database.Accounts_db.acc_details(classes.Log_in.Login.User_ID)
                            mmid=functionality.Gen_Captcha.mmid_gen()
                            uid=functionality.gen_uid.generate_uid(classes.Log_in.Login.User_ID)
                            new_account_no=input("New Account No: ")
                            existing=database.Accounts_db.existing_Account()
                            while new_account_no in existing:
                                print("Account number already exists,Please try again")
                                new_account_no=input("New Account No: ")
                            try:
                                validations.Validations.validate_acct_no(new_account_no)
                                new_ifsc=functionality.Gen_Captcha.gen_ifsc()
                                exists=database.Accounts_db.existing_ifsc()
                                while new_ifsc in exists:
                                    print("IFSC already exists,Please try again")
                                    new_ifsc=input("New IFSC: ")
                                database.Accounts_db.set_rd_fd(classes.Log_in.Login.User_ID,new_account_no,new_ifsc,uid,'FD',option4,'NULL',mmid)
                            except:
                                print('Please enter valid no. of months')
                                new_account()
                        database.Accounts_db.set_balance(classes.Log_in.Login.User_ID,option4)
                        print("Debiting account number:"+str(new_detail[1]))
                        print("Account opened successfully")
                        new_account()
                    elif(option5=="N"or option5=="n"):
                        new_account()
                    else:
                        print("Wrong choice entered")
                        new_account()                   
                else:
                    print("Insufficient balance")
                    classes.Options.options()
            else:
                print("Invalid Amount,try again")
                new_account()    
        else:
            print("Enter valid Account type")
            new_account()            
    elif(option2!="N" and option2!="n"):
        print("Enter Valid Choice: ")
        new_account()
    else:
        classes.Options.options()