import classes.Log_in,classes.Register,classes.Report
class Menu:
    def __init__(self):
        '''This module displays a menu to the user.'''
        print("+------------------------+")
        print("| Welcome to PyMobile    |")
        print("+------------------------+")
        print("Choose an Option from below:\n")
        end=False
        while(end==False):
            print("1. Login\n2. Register\n3. Report\n4. About Us\n5. Exit")
            option=input()
            if(option=='1'):
                print("Login")
                classes.Log_in.Login()
            elif(option=='2'):
                print("Register")
                classes.Register.Register()
            elif(option=='3'):
                classes.Report.Report()
            elif(option=='4'):
                print('Group no #\nGroup Members:\n-----------------\n1. Pratik Mohare\n2. XYZ \n3. PQR\n4. IJK\n\n')
            elif(option=='5'):
                print("Thank You")
                end=True
            else:
                print("Please enter a valid option (1,2,3,4,5)")