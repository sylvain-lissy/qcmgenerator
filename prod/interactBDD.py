
import mariadb
import json

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'pwd',
    'database': 'data'
}


def getQCMs():
    conn = mariadb.connect(**config)
    cur = conn.cursor()
    cur.execute("select * from qcm")

    description=cur
    conn.close

    return description


