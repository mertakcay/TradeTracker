

class PostgresHelper():
    def __init__(self, database_username, database_password, database_name):
        self._database_username = database_username,
        self._database_password = database_password,
        self._database_name = database_name
        self._conn =  psycopg2.connect(
                        host='localhost',
                        port=5432,
                        dbname=self._database_name,
                        user=self._database_username,
                        password=self._database_password ) 
        
    
    def return_connect(self):
        return self._conn
    