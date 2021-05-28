import os
import datetime
import pymysql

# Get username from Cloud9 workspace
# (modify this variable if running on another environment)
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        rows = [("Bob", 21, "1990-02-06 23:04:56"),
               ("Jim", 56, "1956-05-09 13:12:45"),
               ("Nello", 51, "1961-04-25 18:06:35")]
        cursor.executemany("INSERT INTO Friends VALUES (%s, %s, %s);", rows)
        connection.commit()
finally:
    # Close the connection, regardless of whether or not the above was success
    connection.close() 