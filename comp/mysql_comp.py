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
    host='rm-uf6yh3m14z6il3lv8xo.mysql.rds.aliyuncs.com',
    port=3306,
    user='astra',
    password='Shoot4themoon',
    database='astra',
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


def mysql_login(input_id, input_pswd):
    rslt = "Not logged in"
    result = mysql_data_read('*', 'account')

    id = []
    password = []
    name = []

    for i in range(len(result)):
        id.append(result[i]['id'])
        password.append(result[i]['password'])
        name.append(result[i]['name'])

    for j in range(len(result)):
        if input_id == '':
            rslt = "Not logged in"
            noti = "Please enter name"
            break
        elif input_id != '' and input_pswd == '':
            rslt = "Not logged in"
            noti = "Please enter password"
            break
        elif id[j] == input_id and password[j] == input_pswd:
            rslt = name[j]
            noti = "Successful"
            break
        elif id[j] == input_id and password[j] != input_pswd:
            rslt = "Not logged in"
            noti = "Password error"
            break
        else:
            rslt = "Not logged in"
            noti = "Name not found，please contact customer service"

    return rslt, noti