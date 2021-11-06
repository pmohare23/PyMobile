import random
def generate_uid(str1):
    uid=str1[0]
    l1=['~','!','@','#','$','%','^','&']
    i=random.randrange(0,7)
    uid+=l1[i]
    n=random.randrange(100,999)
    uid+=str(n)
    return uid