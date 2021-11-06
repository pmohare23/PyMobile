import validations.Validations
import functionality.Gen_Captcha
import functionality.gen_uid
from database.Register_Db import acct_is_unique, UserID_is_unique,\
    UniqueID_is_unique, mmid_is_unique, update_USERDETAILS_table, update_BANK_table  
from exceptions.exceptions import InvalidAcctNoException,\
    InvalidAcctNameException, InvalidAmountException, InvalidMobileNoException,\
    InvalidMmidException, InvalidPasswordException, InvalidUidException
import functionality.Payee
class Register:
    def __init__(self):
        list_of_valid_accno=[996995108126, 299150722147, 582291052161, 844861087217, 193235270733, 246898538529, 913070086600, 230137390731, 578499748099, 423324581625, 477353156853, 240648175254, 420121491306, 480264065762, 404115052617, 168249983022, 455277626565, 178213397874, 132910849488, 307368331372, 867245079620, 410281677708, 891076562573, 446435236292, 765530886938, 226426263874, 521472200341, 562912316989, 530530483970, 141595620050, 270019935306, 896573428223, 504791175130, 867620593842, 106656715695, 647389506359, 963764394466, 901839981893, 688381855223, 374471364892, 486339949122, 396356142011, 269631086826, 593620202964, 272587233185, 117734794245, 371936588904, 691817216879, 489883618006, 702745105982, 314531522779, 378289699494, 270815701826, 650877369057, 261921441479, 275320499601, 894837755760, 516922392822, 461978975157, 125502610346, 946261248713, 983740819778, 357469341647, 948157759295, 400460560163, 259864774226, 434997475123, 750328049924, 207105364608, 445415175080, 229999356771, 549191081322, 561769302140, 127834304452, 495324100378, 580855994894, 559301151412, 122090370239, 459580327137, 980568934788, 522174043358, 143337410687, 477404168351, 381237569543, 669991284400, 127670908811, 324844307748, 260524760194, 230639951220, 150989253884, 699235796947, 707814857214, 676519567725, 336454434028, 881819525465, 573953202907, 294630150482, 488590630749, 516463617229, 475117921215]
        try:
            
            name=input("Account Name:")
            validations.Validations.validate_acct_name(name)
                        
            acct_no=input("Account number:")
            validations.Validations.validate_acct_no(acct_no)
            
            if int(acct_no) in list_of_valid_accno:
                pass
            else:
                print("Unregistered Account number")
                Register.__init__(self)
                
            mob_no=input("Mobile no:")
            validations.Validations.validate_mob_no(mob_no)
            
                
            if not acct_is_unique(acct_no):
                print("Account No. already exist!")
                Register.__init__(self)
             
            while True:    
                userid=input("User Id:")
                if not UserID_is_unique(userid):
                    print("User id already exists! Choose another username")
                    continue
                else:
                    break 
                
            while True:
                pswd=input("Password")
                if not validations.Validations.validate_password(pswd):
                    print("Incorrect password format. Re-enter password")
                    continue
                else:
                    break
                
            while True:
                def_captcha=functionality.Gen_Captcha.generate_captcha()
                captcha=input("Enter captcha: "+def_captcha)
                if captcha==def_captcha:
                    break
                print("Captcha do not match. Re-enter captcha")
            
            while True:
                
                uid=functionality.gen_uid.generate_uid(name)
                if UniqueID_is_unique(uid):
                    break
            
            print("Registered Successfully. Your unique id is: "+str(uid))
            
            
            change=input("Do you wish to change(Y/N):")
            if(change.upper()=='Y'):
                while True:
                    uid=input("Enter a new unique id:")
                    if validations.Validations.validate_uid(uid,name) and UniqueID_is_unique(uid):
                        break
                    print("Unique id format is wrong. Re-enter unique id")
                    
                print("Unique id changed")
            
            while True:
                mmid=functionality.Gen_Captcha.mmid_gen()
                if mmid_is_unique(mmid):
                    break  
            ifsc=functionality.Gen_Captcha.gen_ifsc()  
            update_USERDETAILS_table(userid, name, mob_no, pswd)
            update_BANK_table(acct_no, userid,name,uid,mmid,ifsc) 
            functionality.Payee.Payee(userid, acct_no)
            
                        
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
        except InvalidPasswordException as e:
            print(e)
        except InvalidUidException as e:
            print(e)
        except Exception as e:
            print("Sorry. Some system error occurred")
            print(e)