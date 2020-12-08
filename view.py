from controler import *

def view_menu():
    print('1 - delete , 2 - update , 3 - insert , 4 - rand , 5 - search')
    return int(input('Input number of request:'))

def column_db():
    return input('Input column name: ')

def table_db():
    return input('Input table name: ')

def value_old():
    return input('Enter old value: ')

def value_new():
    return input('Enter new value: ')

def value_db():
    return input('Enter value: ')

def value_db_int():
    return int(input('Enter int(value):')