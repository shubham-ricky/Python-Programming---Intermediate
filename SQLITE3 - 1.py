"""
You are to write a Python program to import the data in c1059c_cwf_q2.csv into the SQLITE3 database. Your program should do the following tasks: 

a)	Create the language table. 
b)	Ensure the primary keys and foreign key (if any) are properly defined.
c)	Open the data file c1059c_cwf_q2.csv. 
d)	For each entry in the data file, insert them into the database table.

"""

import csv
import sqlite3

conn = sqlite3.connect("language.db")
try:
    conn.execute("drop table language")
except sqlite3.OperationalError as e:
    print(e)
    
sq1 = """CREATE TABLE language
    (id INTEGER PRIMARY KEY, 
    's/n' INTEGER NOT NULL, 
    language TEXT NOT NULL,
    recommend1 TEXT NOT NULL, 
    recommend2 TEXT NOT NULL, 
    recommend3 TEXT NOT NULL, 
    rating FLOAT NOT NULL, 
    trend FLOAT NOT NULL)"""
conn.execute(sq1)                                           #...Task a): Create the language table            
                                                            #...Task b): Ensure the primary keys and foreign key (if any) are properly defined
languagereader = csv.reader(open("c1059c_cwf_q2.csv"))      #... Task c): Open the .csv file

#remove the title
next(languagereader)

for data in languagereader:
    sq1 = """INSERT INTO language ('s/n', language, recommend1, recommend2, recommend3, rating, trend) 
    VALUES ('%s', '%s', '%s','%s', '%s', '%s', '%s')""" %(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
    cursor = conn.execute(sq1)                              #...Task d): For each entry in the data file, insert them into the database table    
        
conn.commit()



