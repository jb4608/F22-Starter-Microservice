import pymysql

import os


class ColumbiaStudentResource:

    def __int__(self):
        pass

    @staticmethod
    def _get_connection():
        user = os.environ.get("DBUSER"),
        password = os.environ.get("DBPW"),
        host = os.environ.get("DBHOST"),

        conn = pymysql.connect(
            user= "root",
            password= "dbuserdbuser",
            host=  "e61561.cvkl7vplx30l.us-east-1.rds.amazonaws.com",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    @staticmethod
    def get_by_key(key):

        sql = "SELECT * FROM f22_databases.columbia_students where auto_id=%s";
        conn = ColumbiaStudentResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

