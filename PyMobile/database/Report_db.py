from utility.DBConnectivity import create_connection,create_cursor
def report():
    try:
        list_nos=[]
        con=create_connection()
        cur=create_cursor(con)
        cur.execute('Select MobileNo from USERDETAILS')
        for i in cur:
            list_nos.append(i[0])
    except:
        print('Unable to fetch Mobile Numbers')
    finally:
        cur.close()
        con.close()
    return list_nos