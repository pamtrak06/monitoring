#!/usr/bin/python
import mysql.connector
import os

def init():
    """ Connect to the Mysql database server """
    mydb = None
    try:
 
        # connect to the Mysql server
        print('Connecting to the Mysql database...')
        mydb = mysql.connector.connect(
          host=os.environ['DATABASE_HOST'],
          user=os.environ['DATABASE_USER'],
          passwd=os.environ['DATABASE_PASSWORD']
        )
 
        # create a cursor
        mycursor = mydb.cursor()

        # display the Mysql database server version
        print('Mysql database version:')
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(db_version)
        
        # execute a statement
        print('Mysql database initialization:')
        mycursor.execute("CREATE DATABASE %s", os.environ['DATABASE_NAME'])
        mycursor.execute("CREATE USER %s@%s IDENTIFIED BY '%s'", os.environ['DATABASE_USER'], os.environ['DATABASE_HOST'], os.environ['DATABASE_PASSWORD'])
        mycursor.execute("GRANT ALL PRIVILEGES ON %s.* TO %s@%s", os.environ['DATABASE_NAME'], os.environ['DATABASE_USER'], os.environ['DATABASE_HOST'])
        mycursor.execute("FLUSH PRIVILEGES")
        mydb.commit()
      
        # close the communication with the Mysql
        mycursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if mydb is not None:
            mydb.close()
            print('Mysql database connection closed.')
 
 
if __name__ == '__main__':
    init()
