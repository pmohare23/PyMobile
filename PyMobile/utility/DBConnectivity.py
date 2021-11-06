import cx_Oracle
def create_connection():
    return cx_Oracle.Connection('')
def create_cursor(con):
    return cx_Oracle.Cursor(con)