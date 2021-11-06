from utility.DBConnectivity import create_connection,create_cursor
def fetch_trans(accno):
    try:
        list_tra=[]
        con=create_connection()
        cur=create_cursor(con)
        cur.execute('Select B.AccName,T.TDate,T.TType,T.AmtTrans,T.Trans_acc from Transactions T inner join Bank B on T.Trans_acc=B.AccNo where T.AccNo='+str(accno)+' Order By T.Tdate Desc')
        for i in cur:
            list_tra.append(i)
    except:
        print('Unable to fetch Transactions')
    finally:
        cur.close()
        con.close()
    if(len(list_tra)>4):
        list_tra=list_tra[:4]
    return list_tra
def insert_trans(accno,trans_acc,amount,ty):
    try:
        con=create_connection()
        cur=create_cursor(con)
        cur.execute('Insert into Transactions Values('+str(accno)+','+str(trans_acc)+','+str(amount)+',SYSDATE,\''+ty+'\')')
        con.commit()
    except:
        print('Unable to add Transaction')
    finally:
        cur.close()
        con.close()
def fetch_accounts(User_ID):
    try:
        account_list=[]
        count=1
        con=create_connection()
        cur=create_cursor(con)
        cur.execute('SELECT AccNo,AccType,AccName,AccBalance FROM BANK WHERE UserID =\''+User_ID+'\' ORDER BY CreationTime DESC')
        for i in cur:
            account_list.append(i)
            count+=1
    except:
        print("Error in fetching details")
    finally:    
        cur.close()
        con.close()
    return account_list