import psycopg2 
from psycopg2 import errors
import sys
import time



def information(table_name,column_name):
    conn = psycopg2.connect(dbname='DB',user='postgres',password='12345',host='localhost',port=5432)
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    cur.execute(f"SELECT {column_name} FROM {table_name}")
    values=cur.fetchall()
    print(values)
    
    cur.close()
    conn.close()

def update_DB(table_name,column_name,new,old):
    conn = psycopg2.connect(dbname='DB',user='postgres',password='12345',host='localhost',port=5432)
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    if column_name == 'cost' or 'cashbox' or 'money' :
        try:
            cur.execute(f"UPDATE {table_name} SET {column_name} = {new} WHERE {column_name} = {old} ")
        except psycopg2.Error as error:
            print(error.pgcode)
            print(f'{error}')

    else:
         try:
            cur.execute(f"UPDATE {table_name} SET {column_name} = %s WHERE {column_name} = %s ",(new,old))
         except psycopg2.Error as error:
            print(error.pgcode)
            print(f'{error}')

    cur.close()
    conn.close()

def insert_DB(table_name,size):
    conn = psycopg2.connect(dbname='DB',user='postgres',password='12345',host='localhost',port=5432)
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    mass = []

    if size == 2:
        for key in range(0,size):
            mass.append(input())
        try:
            cur.execute(f"INSERT INTO {table_name} VALUES ('{mass[0]}', '{mass[1]}')")
        except psycopg2.Error as error:
            print(error.pgcode)
            print(f'{error}')
    elif size == 3 :
        for key in range(0,size):
            mass.append(input())
        try:
            cur.execute(f"INSERT INTO {table_name} VALUES ('{mass[0]}', '{mass[1]}' , '{mass[2]}')")
        except psycopg2.Error as error:
            print(error.pgcode)
            print(f'{error}')

    cur.close()
    conn.close()

def delete_DB(table_name,column_name,value):
    conn = psycopg2.connect(dbname='DB',user='postgres',password='12345',host='localhost',port=5432)
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    if column_name == 'cost' or 'cashbox' or 'money' :
        try:
            cur.execute(f"DELETE FROM {table_name} WHERE {column_name} = {value} ")
        except psycopg2.Error as error:
            print(error.pgcode)
            print(f'{error}')

    else:
         try:
            cur.execute(f"DELETE FROM {table_name} WHERE {column_name} = %s ",(value))
         except psycopg2.Error as error:
            print(error.pgcode)
            print(f'{error}')

    cur.close()
    conn.close()



def random_DB(table_name,size):
    conn = psycopg2.connect(dbname='DB',user='postgres',password='12345',host='localhost',port=5432)
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    if table_name == 'shopper':
        cur.execute(f"INSERT INTO shopper SELECT chr(trunc(65+random() * 15000)::int),(trunc(65+random() * 15000)::int),chr(trunc(65+random() * 15000)::int) FROM generate_series(1,{size})")
    elif table_name == 'shelf_life':
        cur.execute(f"INSERT INTO shelf_life SELECT chr(trunc(65+random() * 15000)::int),chr(trunc(65+random() * 15000)::int) FROM generate_series(1,{size})")
    elif table_name == 'seller':
        cur.execute(f"INSERT INTO seller SELECT chr(trunc(65+random() * 15000)::int),chr(trunc(65+random() * 15000)::int),(trunc(65+random() * 15000)::int) FROM generate_series(1,{size})")
    elif table_name == 'product':
        cur.execute(f"INSERT INTO product SELECT chr(trunc(65+random() * 15000)::int),(trunc(65+random() * 15000)::int) FROM generate_series(1,{size})")

    cur.close()
    conn.close()

def search_DB(count):
    conn = psycopg2.connect(dbname='DB',user='postgres',password='12345',host='localhost',port=5432)
    cur = conn.cursor()

    column=[]
    for k in range(0,count):
        column.append(str(input(f"Input name of the attribute number {k+1} to search by : ")))
    print(column)
    tables = []
    types = []
    if count == 2:
        curso_names_str = f"SELECT table_name FROM INFORMATION_SCHEMA.COLUMNS WHERE information_schema.columns.column_name LIKE '{column[0]}' INTERSECT ALL SELECT table_name FROM information_schema.columns WHERE information_schema.columns.column_name LIKE '{column[1]}'"
    else:
        curso_names_str = "SELECT table_name FROM INFORMATION_SCHEMA.COLUMNS WHERE information_schema.columns.column_name LIKE '{}'".format(column[0])
    print("\ncol_names_str:", curso_names_str)
    cur.execute(curso_names_str)
    curso_names = (cur.fetchall())
    for tupl in curso_names:
        tables += [tupl[0]]

    for s in range(0,len(column)):
        for k in range(0,len(tables)):
            cur.execute(f"SELECT data_type FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name='{tables[k]}' AND column_name ='{column[s]}'")
            type=(cur.fetchall())
            for j in type:
                types+=[j[0]]
    print(types)
    if count == 1:
        if len(tables) == 1:
            if types[0] == 'character varying':
                i_char = input(f"Input string for {column[0]} to search by : ")
                start=time.time()
                cur.execute(f"SELECT * FROM {tables[0]} WHERE {column[0]} LIKE '{i_char}'")
                print(cur.fetchall())
                print("TIME = %s seconds"%(time.time()-start))
            elif types[0] == 'integer':
                left_limits = input("Enter left limit ")
                right_limits = input("Enter right limit ")
                start=time.time()
                cur.execute(f"SELECT * FROM {tables[0]} WHERE {column[0]}>='{left_limits}' AND {column[0]}<'{right_limits}'")
                print(cur.fetchall())
                print("TIME = %s seconds"%(time.time()-start))
        elif len(tables) == 2:
            if types[0] == 'character varying':
                i_char = input(f"Input string for {column[0]} to search by : ")
                start = time.time()
                cur.execute(f"SELECT {column[0]} FROM {tables[0]} WHERE {column[0]} LIKE '{i_char}' UNION ALL SELECT {column[0]} FROM {tables[1]} WHERE {column[0]} LIKE '{i_char}'")
                print(cur.fetchall())
                print("TIME = %s seconds" % (time.time() - start))
            elif types[0] == 'integer':
                left_limits = input("Enter left limit ")
                right_limits = input("Enter right limit ")
                start = time.time()
                cur.execute(f"SELECT {column[0]} FROM {tables[0]} WHERE {column[0]}>='{left_limits}' AND {column[0]}<'{right_limits}' UNION ALL SELECT {column[0]} FROM {tables[1]} WHERE {column[0]}>='{left_limits}' AND {column[0]}<'{right_limits}' ")
                print(cur.fetchall())
                print("TIME = %s seconds" % (time.time() - start))

    elif count == 2:
        if len(tables) == 1:
            if types[0] == 'character varying' and types[1] == 'character varying':
                i_char = input(f"Input string for {column[0]} to search by : ")
                o_char = input(f"Input string for {column[1]} to search by : ")
                start = time.time()
                cur.execute(f"SELECT * FROM {tables[0]} WHERE {column[0]} LIKE '{i_char}' AND {column[1]} LIKE '{o_char}' ")
                print(cur.fetchall())
                print("TIME = %s seconds" % (time.time() - start))
            elif types[0] == 'character varying' and types[1] == 'integer':
                i_char = input(f"Input string for {column[0]} to search by : ")
                left_limit = input(f"Enter left limit for {column[1]} ")
                right_limit = input(f"Enter right limit for {column[1]} ")
                start = time.time()
                cur.execute(f"SELECT * FROM {tables[0]} WHERE {column[0]} LIKE '{i_char}' AND {column[1]}>='{left_limit}' AND {column[1]}<'{right_limit}'")
                print(cur.fetchall())
                print("TIME = %s seconds" % (time.time() - start))
            elif types[0] == 'integer' and types[1] == 'character varying':
                left_limit = input(f"Enter left limit for {column[0]} ")
                right_limit = input(f"Enter right limit for {column[0]} ")
                i_char = input(f"Input string for {column[1]} to search by : ")
                start = time.time()
                cur.execute(f"SELECT * FROM {tables[0]} WHERE {column[0]}>='{left_limit}' AND {column[0]}<'{right_limit}' AND {column[1]} LIKE '{i_char}'")
                print(cur.fetchall())
                print("TIME = %s seconds" % (time.time() - start))
            elif types[0] == 'integer' and types[1] == 'integer':
                left_limit = input(f"Enter left limit for {column[0]} ")
                right_limit = input(f"Enter right limit for {column[0]} ")
                leftLimit = input(f"Enter left limit for {column[1]} ")
                rightLimit = input(f"Enter right limit for {column[1]} ")
                start = time.time()
                cur.execute(f"SELECT * FROM {tables[0]} WHERE {column[0]}>='{left_limit}' AND {column[0]}<'{right_limit}' AND {column[1]}>='{leftLimit}' AND {column[1]}<'{rightLimit}' ")
                print(cur.fetchall())
                print("TIME = %s seconds" % (time.time() - start))

    cur.close()
    conn.close()