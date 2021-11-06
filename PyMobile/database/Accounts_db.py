from utility.DBConnectivity import create_connection, create_cursor
def fetch_accounts(User_ID):
    try:
        account_list=[]
        count=1
        con=create_connection()
        cur=create_cursor(con)
        cur.execute('SELECT AccNo,AccType,AccName,AccBalance FROM BANK WHERE UserID =\''+User_ID+'\' ORDER BY CreationTime DESC')
        for i in cur:
            account_list.append(i)
            print(str(count)+". "+str(i[0])+": "+str(i[1]))
            count+=1
    except:
        print("Error in fetching details")
    finally:    
        cur.close()
        con.close()
    return account_list
def existing_Account():
    try:
        existing_list=[]
        con=create_connection()
        cur=create_cursor(con)
        cur.execute('SELECT AccNo,AccName FROM BANK')
        for i in cur:
            existing_list.append(str(i[0]))
    except:
        print("Error in checking existing accounts")
    finally:    
        cur.close()
        con.close()
    return existing_list
def existing_ifsc():
    try:
        exists_ifsc=[]
        con=create_connection()
        cur=create_cursor(con)
        cur.execute('SELECT IFSC FROM BANK')
        for i in cur:
            exists_ifsc.append(i)
    except:
        print("Error in checking existing IFSC")
    finally:
        cur.close()
        con.close()
    return exists_ifsc
def get_balance(User_ID):
    try:
        bal=0
        con=create_connection()
        cur=create_cursor(con)
        cur.execute("Select AccBalance FROM BANK WHERE AccType='Savings' AND AccNo in (SELECT AccNo FROM BANK WHERE UserID =\'"+User_ID+"\')")
        for i in cur:
            bal=int(i[0])
    except:
        print("Error in fetching existing balance from Savings Account")
    finally:
        cur.close()
        con.close()
    return bal
def set_balance(User_ID,amount):
    try:
        con=create_connection()
        cur=create_cursor(con)
        cur.execute('UPDATE BANK SET AccBalance=AccBalance-'+str(amount)+' where AccType=\'Savings\' and UserID=\''+User_ID+'\'')
        con.commit()
    except:
        print("Error in updating balance")
    finally:
        cur.close()
        con.close()
def set_rd_fd(User_ID,new_account_no,new_ifsc,uid,option3,amount,option6,mmid):
    try:
        con=create_connection()
        cur=create_cursor(con)
        cur.execute('INSERT INTO BANK (UserID,AccNo,AccName,IFSC,UniqueID,AccType,AccBalance,Months,MMID) VALUES(\''+User_ID+'\','+str(new_account_no)+',\''+User_ID+'\',\''+new_ifsc+'\',\''+str(uid)+'\',\''+option3+'\','+str(amount)+','+str(option6)+','+str(mmid)+')')
        con.commit()
    except:
        print("Error in creating account")
    finally:
        cur.close()
        con.close()
def acc_details(User_ID):
    try:
        account=''
        con=create_connection()
        cur=create_cursor(con)
        cur.execute("SELECT AccName,AccNo FROM BANK WHERE UserID =\'"+User_ID+"\'AND AccType='Savings'")
        for i in cur:
            account=i
    except:
        print("Error in fetching Account details from Savings Account")
    finally:
        cur.close()
        con.close()
    return account