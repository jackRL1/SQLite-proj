import sqlite3
import time
import datetime
import random

# creates a connection and database file to store tables. 
conn = sqlite3.connect('example.db')

# cursor object. 
c = conn.cursor()

#method for creating a table. 
def creat_table():
    c.execute('CREATE TABLE IF NOT EXISTS newTable(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')

#simple data entry method
def data_entry():
    c.execute("INSERT INTO newTable VALUES(213, '2019-03-15', 'Python', 45)")
    conn.commit()
    c.close()
    conn.close()

#dynamic data entry for adding data and time stamp, code used, and random generated value.
def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,100)
    #list of tuples that are being added to the database
    adding = [(unix, date, keyword, value)]
    #inserts the values from adding into the data table. 
    c.executemany('INSERT INTO newtable VALUES (?, ?, ?, ?)', adding)
    #commits changes to the table
    conn.commit()


# method for reading the rows of information from a database
def print_bd_rows():
    c.execute('SELECT * FROM newTable')
    for row in c.fetchall():
        print(row)


# reads and prints all unix timestaps larger than the one specified in the method.
def read_from_db():
    c.execute('SELECT * FROM newTable WHERE unix > 1553118039')
    #data = c.fetchall()
    #print(data)
    for row in c.fetchall():
        print(row)



#Function call for the creating a table called newTable
creat_table()



# For loop to generate data inserted into the newTable
for i in range(10):
    dynamic_data_entry()
    time.sleep(0.5)


print_bd_rows()

read_from_db()




#closes the connection and cursor. 
c.close()
conn.close()
