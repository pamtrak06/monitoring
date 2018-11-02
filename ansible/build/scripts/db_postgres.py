#!/usr/bin/python
import psycopg2
import os
 
def init():
    """ Connect to the PostgreSQL database server """
    mydb = None
    try:
 
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        mydb = psycopg2.connect(
          host=os.environ['DATABASE_HOST'],
          user=os.environ['DATABASE_USER'],
          passwd=os.environ['DATABASE_PASSWORD']
        )
 
        # create a cursor
        mycursor = mydb.cursor()
        
        # display the PostgreSQL database server version
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(db_version)
        
        # execute a statement
        print('PostgreSQL database initialization:')
        mycursor.execute("CREATE ROLE %s WITH LOGIN PASSWORD '%s'", os.environ['DATABASE_USER'], os.environ['DATABASE_PASSWORD'])
        mycursor.execute("CREATE DATABASE %s OWNER %s", os.environ['DATABASE_NAME'], os.environ['DATABASE_USER'])
        mycursor.execute("GRANT ALL ON DATABASE %s TO %s", os.environ['DATABASE_NAME'], os.environ['DATABASE_USER'])
 
     
     # close the communication with the PostgreSQL
        mycursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if mydb is not None:
            mydb.close()
            print('PostgreSQL database connection closed.')
 
 
if __name__ == '__main__':
    init()


