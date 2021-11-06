import re
from exceptions.exceptions import InvalidAcctNoException,\
    InvalidAcctNameException, InvalidAmountException, InvalidMobileNoException,\
    InvalidMmidException, InvalidNoOfMonthsException
    
def validate_acct_no(acct_no):
    if not(acct_no.isdigit() and len(acct_no)==12):
        raise InvalidAcctNoException()
def validate_acct_name(acct_name):
    if not(acct_name.isalpha() and len(acct_name)<=20):
        raise InvalidAcctNameException()
def validate_mob_no(mob_no):
    if not (mob_no.isdigit() and len(mob_no)==10):
        raise InvalidMobileNoException()
def validate_password(password):
    if re.search(r"[A-Z]",password) and re.search(r"[a-z]",password) and not (password.isalnum()) and re.search(r"/s",password)==None and re.search(r"[0-9]",password):
        return True
    return False
def validate_uid(uid,name):
    if uid.startswith(name[0]) and not uid[1].isalnum() and re.search(r"\d{3}$",uid):
        return True
    return False
def validate_mmid(mmid):
    if not(mmid.isdigit() and len(mmid)==6):
        raise InvalidMmidException()
def validate_amount(amount):
    if not amount.isdigit():
        raise InvalidAmountException()
def validate_expression(ans):
    if ans.isdigit() or (ans[0]=='-' and  ans[1:].isdigit()):
        return True
    return False
def validate_no_of_months(no_of_months):
    if not(no_of_months.isdigit() and int(no_of_months)>0):
        raise InvalidNoOfMonthsException()