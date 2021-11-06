import classes.Options
import classes.Log_in
import database.login_db
import database.View_db
class Fund_Transfer:
    def __init__(self):
        Option_FundTransfer = input("Fund Transfer\n1. Transfer through Account No\n2. Transfer through MMID\n---Press any other key for back---")
        User_details=database.login_db.get_details(classes.Log_in.Login.User_ID)
        if Option_FundTransfer=="1":
            AccNo = input("Enter Account No: ")
            AccName = input("Enter Account Name: ")
            IFSC = input("Enter IFSC Code: ")
            AmntTrnsfr = input("Enter Amount to be transfered: ")
            acdetails=database.login_db.fun_transfer_acc(AccNo)
            if AccName==acdetails[0] and IFSC==acdetails[1]:
                Confirm = input("Confirm(Y/N): ")
                if (Confirm.upper()=="Y"):
                    if int(AmntTrnsfr)<=User_details[1]:
                        UniqueID = input("Please enter the unique ID to transfer: ")
                        if (UniqueID==acdetails[2]):
                            database.login_db.transfer_amount(User_details[0],AccNo,AmntTrnsfr)
                            database.View_db.insert_trans(User_details[0],AccNo,AmntTrnsfr,'IFD')
                            print ("Amount transfered successfully")
                            classes.Options.options()
                        else:
                            print ("Invalid Unique ID")
                            Fund_Transfer()
                    else:
                        confirmation = input("Insufficient Fund.Transfer failed\n.Do you wish to continue(Y/N): ")
                        if confirmation.upper()=="Y":
                            Fund_Transfer()                        
            else:
                print ("Incorrect Account Details")
                Fund_Transfer()  
        elif Option_FundTransfer=="2":
            MMID = input("Enter MMID code: ")
            MobileNo = input("Enter MobileNo: ")
            UniqueID = input("Enter UniqueID: ")
            AmntTrnsfr = input("Enter Amount to be transfered: ")
            acdetails=database.login_db.fun_transfer_mm(MMID)
            if MobileNo==acdetails[0] and UniqueID==acdetails[1]:
                Confirm=input("Confirm(Y/N): ")
                if (Confirm.upper()=="Y"):
                    if int(AmntTrnsfr)<=User_details[1]:
                        database.login_db.transfer_amount(User_details[0],acdetails[2],AmntTrnsfr)
                        database.View_db.insert_trans(User_details[0],acdetails[2],AmntTrnsfr,'MMT')
                        print ("Amount transfered successfully")
                        classes.Options.options()
                    else:
                        confirmation = input("Insufficient Fund.Transfer failed\n.Do you wish to continue(Y/N): ")
                        if confirmation.upper()=="Y":
                            Fund_Transfer()
                else:
                    Fund_Transfer()
            else:
                print ("Incorrect Account Details")
                Fund_Transfer()
        else:
            classes.Options.options()