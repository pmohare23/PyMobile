from utility.DBConnectivity import create_connection,create_cursor
def acct_is_unique(AccNo):
    try:
        con1=create_connection()
        cur1=create_cursor(con1)
        
        cur1.execute("select count(*) from BANK where AccNo="+AccNo)
        for row in cur1:
            if int(row[0])==0:
                return True
            return False
    finally:
        cur1.close()
        con1.close()
        
def UserID_is_unique(UserID):
    try:
        con1=create_connection()
        cur1=create_cursor(con1)
        
        cur1.execute("select count(*) from USERDETAILS where UserID='"+UserID+"'")
        for row in cur1:
            if int(row[0])==0:
                return True
            return False
    finally:
        cur1.close()
        con1.close()
        
def UniqueID_is_unique(UniqueID):
    try:
        con1=create_connection()
        cur1=create_cursor(con1)
        
        cur1.execute("select count(*) from BANK where uniqueid='"+UniqueID+"'")
        for row in cur1:
            if int(row[0])==0:
                return True
            return False
    finally:
        cur1.close()
        con1.close()
        
def mmid_is_unique(mmid):
    try:
        con1=create_connection()
        cur1=create_cursor(con1)
        
        mmid=str(mmid)
        cur1.execute("select count(*) from BANK where mmid="+mmid)
        for row in cur1:
            if int(row[0])==0:
                return True
            return False
    finally:
        cur1.close()
        con1.close()
        
def update_USERDETAILS_table(UserID,name,MobileNo,Password):
    try:
        con1=create_connection()
        cur1=create_cursor(con1)
        cur1.execute('insert into USERDETAILS values (\''+UserID+'\',\''+name+'\',\''+Password+'\','+MobileNo+')')
        con1.commit()
        
    finally:
        cur1.close()
        con1.close()
        
def update_BANK_table(AccNo,UserID,name,UniqueID,mmid,ifsc):
    try:
        con1=create_connection()
        cur1=create_cursor(con1)
        cur1.execute("insert into BANK values ('"+UserID+"',"+AccNo+",'"+name+"','"+ifsc+"','"+UniqueID+"',systimestamp,'Savings',"+str(0)+","+str(0)+","+str(mmid)+")")
        con1.commit()
    finally:
        cur1.close()
        con1.close()
        
def match_MobileNo(AccNo,MobileNo):
    try:
        
        con1=create_connection()
        cur1=create_cursor(con1)
        cur1.execute("select UserID from BANK where AccNo="+AccNo)
        for row in cur1:
            userid=row[0]
            
        cur1.execute("select MobileNo from USERDETAILS where UserID='"+userid+"'")
        for row in cur1:
            if int(MobileNo)==row[0]:
                return True
            return False
              
    finally:
        cur1.close()
        con1.close()
   
        
def match_name(AccNo,name):
    try:
        con1=create_connection()
        cur1=create_cursor(con1)
        
        cur1.execute("select UserID from BANK where AccNo="+AccNo)
        for row in cur1:
            UserID=row[0]
        
        cur1.execute("select Name from USERDETAILS where UserID='"+UserID+"'")
        for row in cur1:
            if name==row[0]:
                return True
            return False
        
    finally:
        cur1.close()
        con1.close()
        
def update_payee_table(nick_name,payee_AccNo,cust_UserID,MobileNo):
    try:
        con1=create_connection()
        cur1=create_cursor(con1)
        
        cur1.execute("select UserID from BANK where AccNo="+payee_AccNo)
        for row in cur1:
            payee_UserID=row[0]
        
        cur2=create_cursor(con1)
        cur2.execute("insert into Payee values ('"+payee_UserID+"','"+nick_name+"',"+payee_AccNo+",systimestamp,'"+cust_UserID+"',"+MobileNo+")")
        con1.commit()
        
    finally:
        cur2.close()
        cur1.close()
        con1.close()