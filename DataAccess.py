import psycopg2
from urllib.parse import urlparse
import os

class DataAccess():

    conn_string = ""
    
    @classmethod
    def getConnectionString(self):
        if self.conn_string=="":
            value=os.environ.get('DATABASE_URL', None)
            if value is not None:
                result = urlparse(value)
                username = result.username
                password = result.password
                database = result.path[1:]
                hostname = result.hostname
                self.conn_string= "host='"+hostname+"' dbname='"+database+"' user='"+username+"' password='"+password+"'"
                return self.conn_string
        else:
            return self.conn_string

    @classmethod
    def execute(self,query):
        print(query)
        conn = psycopg2.connect(self.getConnectionString())
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        cursor.close()

    @classmethod
    def retrieveData(self,query):
        print(query)
        conn = psycopg2.connect(self.getConnectionString())
        cursor = conn.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        cursor.close()
        return records
