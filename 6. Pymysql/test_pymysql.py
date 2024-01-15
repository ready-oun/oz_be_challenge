import pymysql

# (1) db connection
connection = pymysql.connect(
    host = '127.0.0.1',
    password='oz-password',
    db=''
)