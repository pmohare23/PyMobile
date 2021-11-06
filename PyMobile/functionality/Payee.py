import utility.Menu
import validations
from database.Register_Db import acct_is_unique, \
    match_MobileNo, match_name, update_payee_table
from exceptions.exceptions import InvalidAcctNoException,\
    InvalidAcctNameException, InvalidAmountException, InvalidMobileNoException,\
    InvalidMmidException
def Payee(userid,acct_no):
    try:
           
        add_payee_ip=input("Do you want to add payee(Y/N):")
            
        if add_payee_ip.upper()=='Y':
            print("Add Payee:")
            payee_name=input("Account name:")
            validations.Validations.validate_acct_name(payee_name)
            
            payee_acct_no=input("Account number:")
            validations.Validations.validate_acct_no(payee_acct_no)
            
            nick_name=input("Nick name:")
            
            payee_mob_no=input("Mobile no.:")
            validations.Validations.validate_mob_no(payee_mob_no)
            
            if acct_is_unique(payee_acct_no) or not match_MobileNo(payee_acct_no,payee_mob_no) or not match_name(payee_acct_no,payee_name) :
                print("Payee doesn't exist")
                Payee(userid, acct_no)
            
            cnfrm=input("Confirm(Y/N):")
            if cnfrm.upper()=='Y':
                update_payee_table(nick_name,payee_acct_no,userid,payee_mob_no)
                print("Payee added successfully!")
                ip=input("Print Y to go back to main menu or X to exit:")
                if ip.upper()=='Y':
                    Payee(userid, acct_no)
                elif ip.upper()=='X':
                    utility.Menu.Menu()
                    
                    
            else:
                utility.Menu.Menu()
        else:
                utility.Menu.Menu()
                
    except InvalidAcctNoException as e:
        print(e)
    except InvalidAcctNameException as e:
        print(e)
    except InvalidAmountException as e:
        print(e)
    except InvalidMobileNoException as e:
        print(e)
    except InvalidMmidException as e:
        print(e)
    except Exception as e:
        print("Sorry. Some system error occurred")
        print(e)