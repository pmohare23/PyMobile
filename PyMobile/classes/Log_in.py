import random,time
import classes.Options
import database.login_db
class Login:
    count=0
    User_ID=''
    def __init__(self):
        if(Login.count<3):
            Login.User_ID=input("Enter User ID: ")
            User_Password=input("Enter Password: ")
            ops=['+','-','*','//']
            num1=random.randint(0,12)
            num2=random.randint(1,10)
            operation= random.choice(ops)
            value=input("Enter the result for the expression\n"+str(num1)+operation+str(num2)+'= ')
            Actual_Value=eval((str(num1))+ operation+str(num2))
            if value==str(Actual_Value):
                passwd=database.login_db.user_deta(Login.User_ID)
                if User_Password==passwd[0]:
                    classes.Options.options()
                else:
                    print('Wrong credentials')
                    Login.count+=1
                    Login()
            else:
                print('Wrong Evaluation')
                Login.count+=1
                Login()
        else:
            print (" Account is locked Wait for 5 mins")
            time.sleep(300)
            Login.count=0
            Login()