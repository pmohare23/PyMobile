import random
import utility.Menu
import database.Report_db
class Report:
    def __init__(self):
        resp=input('1. Contact Police for emergency\n2. Contact Customer Care\n--Press any other key for back--')
        if(resp=='1'):
            print('Calling Nearest Police Station')
        elif(resp=='2'):
            ticket=random.randrange(100000,999999)
            number=input('Please enter your registered mobile number: ')
            list_nos=database.Report_db.report()
            while int(number) not in list_nos:
                number=input('Number not registered\nPlease enter your registered mobile number: ')
            print('Customer Care will get back to you soon\nPlease note down complaint no. '+str(ticket))
        else:
            utility.Menu.Menu()