from model import *

def controll(request):
    if request == 1:
        table_name = table_db()
        column_name = column_db()
        information(table_name,column_name)
        delete_DB(table_name,column_name,value_db())
    if request == 2:
        table_name = table_db()
        column_name = column_db()
        information(table_name,column_name)
        new=value_new()
        old=value_old()
        update_DB(table_name,column_name,new,old)
    if request == 3:
        table_name=table_db()
        size = value_db_int()
        insert_DB(table_name,size)
    if request == 4:
        table_name=table_db()
        size = value_db()
        random_DB(table_name,size)
    if request == 5:
        search_DB(value_db_int())

controll(view_menu())
