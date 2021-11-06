from validations.Validations import validate_acct_no,validate_acct_name,validate_mob_no,validate_password,validate_uid,validate_mmid,validate_amount,validate_no_of_months
from exceptions.exceptions import InvalidAcctNoException,InvalidAcctNameException,InvalidAmountException,InvalidMobileNoException,InvalidMmidException,InvalidPasswordException,InvalidUidException,InvalidNoOfMonthsException
# Account Number Test
valid1=validate_acct_no('956402123450')
try:
    invalid1=validate_acct_no('561237895210')
    print("The account no is valid")
except InvalidAcctNoException as e:
    print(e)
    
try:
    invalid2=validate_acct_no('425@15421585')
except InvalidAcctNoException as e:
    print(e)
    
# Account Name Test
valid2=validate_acct_name('AmanGupta')
try:
    invalid3=validate_acct_name('Aishwarya')
    print("The account name is valid")
except InvalidAcctNameException as e:
    print(e)
try:
    invalid4=validate_acct_name('Ama@nG!')
except InvalidAcctNameException as e:
    print(e)    
    
# Account Password Test
valid3=validate_password('a@D4')
try:
    invalid5=validate_password('a@D4')
    print("The password is valid")
except InvalidPasswordException as e:
    print(e)
    
# Mobile Number Test
valid4=validate_mob_no('9759822575')
try:
    invalid7=validate_mob_no('9759822575')
    print("The mobile no. is valid")
except InvalidMobileNoException as e:
    print(e)
try:
    invalid8=validate_mob_no('56789a45')
except InvalidMobileNoException as e:
    print(e)
    
#Amount Testing
valid5=validate_amount('500000')
try:
    invalid9=validate_amount('500000')
    print("The amount is valid")
except InvalidAmountException as e:
    print(e)
    
try:
    invalid9=validate_amount('500@000')
except InvalidAmountException as e:
    print(e)
    
#UID Test
valid6=validate_uid('James', 'm@321')  
try:
    invalid10=validate_uid('James', 'm@321')
    print("The Unique id is valid")
except InvalidUidException as e:
    print(e)
    
#MMID Test
valid7=validate_mmid('123456')
try:
    invalid13=validate_mmid('123456')
    print("The MMID is valid")
except InvalidMmidException as e:
    print(e)
    
try:
    invalid14=validate_mmid('12345a')
except InvalidMmidException as e:
    print(e)
    
#Number Of Months Test 
valid8=validate_no_of_months('10')
try:
    invalid15=validate_no_of_months('10')
    print("The No. of months is valid")
except InvalidNoOfMonthsException as e:
    print(e)
    
try:
    invalid16=validate_no_of_months('0')
except InvalidNoOfMonthsException as e:
    print(e)
