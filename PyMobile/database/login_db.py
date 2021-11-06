from utility.DBConnectivity import create_connection, create_cursor
def user_deta(User_ID):
    try:
        pwd_list=[]
        con=create_connection()
        cur=create_cursor(con)
        cur.execute('SELECT Password FROM USERDETAILS WHERE UserID=\''+User_ID+'\'')
        for i in cur:
            pwd_list.append(i[0])
    except:
        print('Failed to fetch User data')
    finally:
        cur.close()
        con.close()
    return pwd_list
def get_details(User_ID):
    try:
        con=create_connection()
        cur=create_cursor(con)
        cur.execute('Select AccNo,AccBalance from Bank where UserID=\''+User_ID+'\' and AccType=\'Savings\'')
        for i in cur:
            details=i
    except:
        print('Error Fetching details')
    finally:
        cur.close()
        con.close()
    return details
def fun_transfer_acc(AccNo):
    try:
        con=create_connection()
        cur=create_cursor(con)
        cur.execute('SELECT AccName,IFSC,UniqueID FROM BANK WHERE AccNo='+AccNo)
        for i in cur:
            transfer=i
    except:
        print('Error Fetching Account details')
    finally:
        cur.close()
        con.close()
    return transfer
def fun_transfer_mm(MMID):
    transfer=0
    try:
        con=create_connection()
        cur=create_cursor(con)
        cur.execute('SELECT U.MobileNo,B.UniqueID,B.AccNo FROM BANK B inner join USERDETAILS U on B.UserID=U.UserID WHERE MMID='+MMID)
        for i in cur:
            transfer=i
    except:
        print('Error Fetching Account details')
    finally:
        cur.close()
        con.close()
    return transfer
def transfer_amount(AccNo_s,AccNo_r,amount):
    try:
        con=create_connection()
        cur=create_cursor(con)
        cur.execute('Update Bank Set AccBalance=AccBalance+'+str(amount)+' where AccNo='+str(AccNo_r))
        con.commit()
        cur.execute('Update Bank Set AccBalance=AccBalance-'+str(amount)+' where AccNo='+str(AccNo_s))
        con.commit()
    except:
        print('Failed to transfer amount')
    finally:
        cur.close()
        con.close()