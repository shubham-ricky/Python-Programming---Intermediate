"""
Write a new Python program to read back the data stored in the database table created in Q2. The following are mandatory tasks that your program should perform: 

a)	Create a dictionary to store ALL programming languages and rating scores as key-value pairs. Display the content of your dictionary. 
b)	List ALL programming languages with rating above 5%.
c)	List ALL programming languages with negative trend. 
d)	Display the TOTAL number of programming languages with rating between 0.5% and 5.0%.  
e)	Display the AVERAGE rating for the top 5 programming languages. Round up your answer to 2 decimal places. 

"""

import sqlite3

conn = sqlite3.connect("language.db")

sq1 = """SELECT * FROM language"""

cursor = conn.execute(sq1)
language_data = cursor.fetchall()

language_pk = {}

for data in language_data:     
    language_pk[data[2]] = data[6]                               #...Task a): Create a dictionary to store ALL programming languages and rating stores as key-value pairs
    
conn.commit()

print()
print("Task a): The contents of the dictionary are:\n",language_pk)       #...Task a): Display the content of the dictionary
print()

sq1 = """SELECT language.language, language.rating FROM language WHERE rating>5 ORDER BY language.rating DESC"""

cursor = conn.execute(sq1)
data = cursor.fetchall()
print("Task b): Programming languages with rating above 5% are:\n",data)  #...Task b): List ALL programming languages with rating above 5%
print()    
    
sq1 = """SELECT language.language, language.trend FROM language WHERE trend<0 ORDER BY language.trend ASC"""

cursor = conn.execute(sq1)
data = cursor.fetchall()
print("Task c): Programming languages with negative trend are:\n",data)   #...Task c): List ALL programming languages with negative trend
print()    
    
sq1 = """SELECT count(*) FROM language WHERE rating>=.5 AND rating<=5"""

cursor = conn.execute(sq1)
data = cursor.fetchall()
print("Task d): The total number of programming languages with rating between 0.5% and 5% both included are:\n",data[0][0])   #...Task d): Display total number of programming languages with rating between 0.5% and 5% both included
print()

sq1 = """SELECT avg(rating) FROM language WHERE rating>6"""

cursor = conn.execute(sq1)
data = cursor.fetchall()
print("Task e): The average rating for top 5 programming languages rounded up to 2 decimal places is:\n",round(data[0][0],2))  #...Task e): Display average rating for top 5 programming languages, round up to 2 decimal places