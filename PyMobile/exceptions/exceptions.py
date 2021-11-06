class InvalidAcctNoException(Exception):
    def __init__(self):
        super().__init__("The account no is invalid")      
class InvalidAcctNameException(Exception):
    def __init__(self):
        super().__init__("The account name is invalid")
class InvalidAmountException(Exception):
    def __init__(self):
        super().__init__("The amount is invalid")
class InvalidMobileNoException(Exception):
    def __init__(self):
        super().__init__("The mobile no. is invalid")
class InvalidMmidException(Exception):
    def __init__(self):
        super().__init__("The MMID is invalid")
class InvalidPasswordException(Exception):
    def __init__(self):
        super().__init__("The password is invalid")
class InvalidUidException(Exception):
    def __init__(self):
        super().__init__("The Unique id is invalid")
class InvalidNoOfMonthsException(Exception):
    def __init__(self):
        super().__init__("The No. of months is invalid")