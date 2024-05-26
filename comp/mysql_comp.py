from datetime import date
from streamlit_option_menu import option_menu
import streamlit as st
import pymysql
from dbutils.pooled_db import PooledDB
import time

MYSQL_DB_POOL = PooledDB(
    creator=pymysql,
    maxconnections=5,
    mincached=2,
    maxcached=3,
    blocking=True,
    setsession=[],
    ping=0,
    host='',
    port=3306,
    user='',
    password='',
    database='',
    charset='utf8'
)


def mysql_data_read(col, table):
    conn = MYSQL_DB_POOL.connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute(f'select {col} from {table}')
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result


def mysql_save(sql, content):
    conn = MYSQL_DB_POOL.connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute(sql, content)
    conn.commit()

    cursor.close()
    conn.close()


def mysql_search(col, table, rA, A, rB, B):
    conn = MYSQL_DB_POOL.connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    if col == '*':
        column_part = '*'
    else:
        column_part = f"`{col}`"

    sql = f"SELECT {column_part} FROM `{table}` WHERE `{rA}`=%s AND `{rB}`=%s"
    cursor.execute(sql, (A, B))
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result


def mysql_login(input_name, input_pswd):
    rslt = "Not logged in"
    result = mysql_search('*', 'account', 'name', input_name, 'password', input_pswd)

    if input_name == '':
        rslt = "Not logged in"
        noti = "Please enter name"
        pswd = 'None'
    elif input_name != '' and input_pswd == '':
        rslt = "Not logged in"
        noti = "Please enter password"
        pswd = 'None'
    elif result == ():
        rslt = "Not logged in"
        noti = "Error，please contact customer service"
        pswd = 'None'
    else:
        rslt = result[0]['name']
        noti = "Successful"
        pswd = result[0]['password']

    return rslt, noti, pswd