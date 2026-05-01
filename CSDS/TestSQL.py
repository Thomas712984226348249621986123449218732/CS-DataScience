from mysql.connector import connect, Error
import MySQLdb
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

# mysql-connector-python (official)
import mysql.connector


def test_mysql_connector():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='tigers',       
            database='datascience'
        )
        if connection.is_connected():
            print("MySQL Connector: Connection successful") 

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")  

@app.route("/")
def index():
    return "Hello, World!", 200



def main():
    test_mysql_connector()



    

if __name__ == "__main__":    
        main()