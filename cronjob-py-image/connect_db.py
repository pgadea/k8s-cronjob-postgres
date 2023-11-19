# ----- Example Python program to insert data into a PostgreSQL database table

import psycopg2

# Open a DB session

dbSession       = psycopg2.connect("dbname='postgres' user='postgres' host='postgress-postgresql' password='1psdDmgCCt' port='5432'");
print("Opened database successfully")
# Open a database cursor

dbCursor = dbSession.cursor()

dbCursor.execute(
'''CREATE TABLE COMPANY
      (ID INT PRIMARY KEY     NOT NULL,
      NAME           TEXT    NOT NULL,
      AGE            INT     NOT NULL,
      ADDRESS        CHAR(50),
      SALARY         REAL);''');

# SQL statement to create a table

sqlCreateTable  = "CREATE TABLE Cities(id bigint, cityname varchar(128), latitude numeric, longitude numeric);";

 

# Execute CREATE TABLE command

dbCursor.execute(sqlCreateTable);

dbSession.commit()
conn.close()


