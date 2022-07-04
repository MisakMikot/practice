import sqlite3

class dbtool():
    def __init__(self, dbname):
        self.dbname = dbname
        self.conn = sqlite3.connect(self.dbname, check_same_thread=False)
        self.cur = self.conn.cursor()

    '''def close(self):
        self.cur.close()
        self.conn.close()'''

    def init(self):
        sqltext = '''CREATE TABLE WIFIS
                        (SSID TEXT,
                        PASSWORD TEXT);'''
        self.cur.execute(sqltext)
        self.conn.commit()

    def search(self, ssid):
        sqltext = 'SELECT * FROM WIFIS WHERE SSID LIKE "' + ssid + '"'
        self.cur.execute(sqltext)
        res = self.cur.fetchall()
        print('Result: ' + str(res))
        return res

    def add(self, ssid, password):
        sqltext = 'SELECT * FROM WIFIS WHERE SSID LIKE "' + ssid + '"'
        self.cur.execute(sqltext)
        res = self.cur.fetchall()
        if len(res) == 0:
            sqltext = 'INSERT INTO WIFIS VALUES ("' + ssid + '", "' + password + '")'
            self.cur.execute(sqltext)
            self.conn.commit()
            print('Added: ' + ssid + ' ' + password)
        else:
            print('Already exists: ' + ssid)