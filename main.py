import mysql.connector
from mysql.connector import errorcode

class MySQLConnect:
    def __init__(self, config):
        self.config = config
        self.cnx = None
    
    def __enter__(self):
        try:
            self.cnx = mysql.conenctor.connect(**self.config)
        except mysql.connector.Error as err:

            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                return None, "access denied"

            if err.errno == errorcode.ER_DBACESS_DENIED_ERROR:
                return None, "DB access denied"
            
            return None, err
        
        return self.cnx, None
    
    def __exit__(self):
        if self.cnx is not None:
            self.cnx.close()

class MySQLOperation:
    def __init__(self, username: str = None, password: str = None):
        self.username = username
        self.password = password

    def set_username(self, username: str):
        self.username = username
    
    def set_password(self, password: str):
        self.password = password
    
    def generate_config(self):
        config = {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'password': 'toor',
            'database': 'mysql'
        }
        return config
    def insert_user_to_db(self, config):
        #config = self.generate_config()
        try:
            with MySQLConnect(config) as cnx:
                cursor = cnx.cursor()
                cmd = f"CREATE USER '{self.username}'@'localhost' IDENTIFIED BY '{self.password}';"
                try:
                    cursor.execute(cmd)
                    cnx.commit()
                    cursor.execute("flush privileges;")
                    print("sucessful")
                    return True
                except:
                    cursor.rollback()
                    print("Unable to execute command")
                    return False
        except:
            print("Unable to conenct")
            return False