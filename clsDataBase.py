import pyodbc


class Databases:

    def __init__(self):
        self.server = 'SQLFILESERVER2\SQL20143'
        print(f'Connect and read data from DB')

    def test(self):
        print(f'List databases on server')

        server = 'SQLFILESERVER\SQLInstanc'
        #database = 'master' # default database

        driver = '{SQL Server}'
        #conn_str = 'DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes'
        conn_str = 'DRIVER='+driver+';SERVER='+server+';Trusted_Connection=yes'

        print('conn_str:', conn_str)

        with pyodbc.connect(conn_str) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT Top 9 name,create_date FROM sys.databases")
                row = cursor.fetchone()
                lp =0
                while row:
                    lp +=1
                    print (lp, str(row[1]) + " => " + str(row[0]))
                    row = cursor.fetchone()
