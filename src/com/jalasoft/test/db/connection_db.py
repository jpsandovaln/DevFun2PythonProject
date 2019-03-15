import os
import sqlite3


class ConnectionDB:
    dbName = "test.db"

    def __init__(self):
        self.__exist = os.path.exists(self.dbName)

    def getConnection(self):
        conn = sqlite3.connect(self.dbName)
        c = conn.cursor()
        if not self.__exist:
            c.execute("CREATE TABLE IF NOT EXISTS PRODUCT(ID integer, name varchar(100), price real, primary key(ID));")

        return conn

