import random 
def generate_captcha():
    l1=['~','!','@','#','$','%','^','&']
    l2=['1','2','3','4','5','6','7','8','9','0']
    l3=['a','b','c','e','p','t','k','q','l','z']
    i=random.randrange(0,7)
    str1=''
    str1+=l3[i]+l1[i]+l2[i]+l3[i+1]+l2[i+1]
    return str1
def mmid_gen():
    mmid=random.randrange(100000,999999)
    return mmid 
def gen_ifsc():
    m=random.randrange(100000,999999)
    ifsc="ASDF"+str(m)
    return ifsc