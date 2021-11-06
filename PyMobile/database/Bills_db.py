from utility.DBConnectivity import create_connection, create_cursor
def paybill_fetchtable(User_ID):
    list_store=[]
    count=1
    try:
        con=create_connection()
        cur=create_cursor(con)
        cur.execute('Select B.AccName,B.AccNo,Bi.BillAmt from BANK B inner join BILLER Bi on B.AccNo=Bi.AccNo where Bi.UserID=\''+User_ID+'\' ORDER BY Bi.BillAmt')
        for i in cur:
            list_store.append(i)
            print(str(count)+". "+str(i[0])+' (Acc No. '+str(i[1])+') Total Amount due- Rs. '+str(i[2]))
            count+=1
    except:
        print('Error Fetching Table. Please try again')
    finally:
        cur.close()
        con.close()    
    return list_store
def get_bal(User_ID):
    balance=0
    try:
        con=create_connection()
        cur=create_cursor(con)
        cur.execute('Select AccBalance from Bank where UserID=\''+User_ID+'\' and AccType=\'Savings\'')
        for i in cur:
            balance=int(i[0])
    except:
        print('Error Fetching Balance. Please try again')
    finally:
        cur.close()
        con.close()
    return balance
def set_bal_bill(User_ID,Acc_Name,bal):
    try:
        con=create_connection()
        cur=create_cursor(con)
        cur.execute('Update BILLER set BillAmt=BillAmt-'+str(bal)+' where UserID=\''+User_ID+'\' and AccNo in (select AccNo from BANK where AccName=\''+Acc_Name+'\')')
        con.commit()
    except:
        print('Error Updating Biller. Please try again')
        raise Exception
    finally:
        cur.close()
        con.close()
def delete_row(User_ID,Acc_Name,bal):
    try:
        con=create_connection()
        cur=create_cursor(con)
        cur.execute('Delete from Biller where BillAmt='+str(bal)+' and UserID=\''+User_ID+'\' and AccNo in (select AccNo from Bank where AccName=\''+Acc_Name+'\')')
        con.commit()
    except:
        print('Error Updating Biller. Please try again')
        raise Exception
    finally:
        cur.close()
        con.close()
def set_bal_Bank(User_ID,bal):
    try:
        con=create_connection()
        cur=create_cursor(con)
        cur.execute('Update Bank set AccBalance=AccBalance-'+str(bal)+' where UserID=\''+User_ID+'\' and AccType=\'Savings\'')
        con.commit()
    except:
        print('Error Updating Balance. Please try again')
        raise Exception
    finally:
        cur.close()
        con.close()
def verify(acc_no,acc_name):
    flag=False
    try:
        con=create_connection()
        cur=create_cursor(con)
        cur.execute('select AccNo,AccName from Bank')
        for ano,name in cur:
            if(ano==acc_no and name==acc_name):
                flag=True
    except:
        print('Error Verifying. Please try again')
    finally:
        cur.close()
        con.close()
    return flag
def bill_fetchtable(User_ID):
    list_store=[]
    try:
        con=create_connection()
        cur=create_cursor(con)
        cur.execute('Select AccNo from BILLER where UserID=\''+User_ID+'\'')
        for i in cur:
            list_store.append(i[0])
    except:
        print('Error Fetching Table. Please try again')
    finally:
        cur.close()
        con.close()    
    return list_store
def bill_update(User_ID,acc_no,amount):
    try:
        con=create_connection()
        cur=create_cursor(con)
        cur.execute('Update Biller Set BillAmt=BillAmt+'+str(amount)+' where UserID=\''+User_ID+'\' and AccNo='+str(acc_no))
        con.commit()
    except:
        print('Error Adding Biller. Please try again')
    finally:
        cur.close()
        con.close()
def bill_add(User_ID,acc_no,amount,acc_type):
    try:
        con=create_connection()
        cur=create_cursor(con)
        cur.execute('Insert into Biller Values(\''+User_ID+'\','+str(acc_no)+','+str(amount)+','+'\''+acc_type+'\')')
        con.commit()
    except:
        print('Error Adding Biller. Please try again')
    finally:
        cur.close()
        con.close()