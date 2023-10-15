import pymysql

MYSQL_HOST = 'localhost'
MYSQL_COMN = pymysql.connect(
    host = MYSQL_HOST,
    port = 3306,
    user = 'dave',
    passwd = 'Rlawlals1029!',
    db = 'blog_db',
    charset = 'utf8'
)

def comn_mysqldb():
    if not MYSQL_COMN.open:
        MYSQL_COMN.plug(reconnect=True)
    return MYSQL_COMN
