import pymysql
import traceback
from xml.etree.ElementTree import parse

class Database(object):
    filename = "database.xml"

    tree = parse(filename)
    root = tree.getroot()

    db_info = {}

    for info in root:
        db_info[info.tag] = info.text.strip()

    user = db_info["user"]
    password = ""
    host = db_info["host"]
    database = db_info["name"]
    port = int(db_info["port"])
    charset = db_info["charset"]


    def __init__(self):
        self.cnx = pymysql.connect(user=self.user, password=self.password, host=self.host, database=self.database, charset=self.charset, port=self.port)
        self.cursor = self.cnx.cursor()
    def query_select(self, sql, values):
        aux = ()
        try:
            query = self.cursor.mogrify(sql,values).replace("=NULL", "IS NULL")
            self.cursor.execute(sql, values)
            aux = self.cursor.fetchall()
        except:
            error = traceback.format_exc()
            print (error)
        finally:
            return aux

    def query_insert(self, sql, values):
        try:
            self.cursor.execute(sql, values)
            self.cnx.commit()
        except:
            error = traceback.format_exc()
            print (error)

    def close_connection(self):

        self.cursor.close()
        self.cnx.close()
