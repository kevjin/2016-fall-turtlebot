#!/usr/bin/python
# -*- coding: utf-8 -*-
#sqltest.py - Fetch and display the MySQL database server version.
# import the MySQLdb and sys modules
#deletes first row, runs after the robot finishes order.
import MySQLdb
import sys
import os
import time
# open a database connection
# be sure to change the host IP address, username, password and database name to match your own
connection = MySQLdb.connect(host = "censored", user = "censored", passwd = "censored", db = "censored")
# prepare a cursor object using cursor() method
cursor = connection.cursor ()
# print the row[0]
# (Python starts the first row in an array with the number zero – instead of one)
reddit=True
checker="dock"
isitthere=True
try: #Selects all the values from the database
	cursor.execute("SELECT * FROM offices LIMIT 10")
	existential=cursor.fetchone()		
	checkit=existential[0] #There are values in the database if this works. This acts as a "checker"
	isitthere=True
except TypeError as error: #There are no values in the database
	#print "false"
	isitthere=False
	connection.commit() #basically updates the database to realtime
connection.commit()
while(reddit and isitthere):	#reddit variable makes sure database is shifted up to the 1st ID, so it can pull the first value, and then it exists the loop	
	try:
        	cursor.execute("SELECT office_id FROM offices WHERE ID='1'")
		row= cursor.fetchone()
        	checker=row[0]
		reddit=False
		connection.commit()
	except TypeError as error:
		reddit=True
        	cursor.execute("SET @i=0")
		cursor.execute("UPDATE offices SET `ID` = @i:=@i+1;")
        	connection.commit()
print checker
if(isitthere): #if this script selected the first value, it is now deleted and everything is shifted up 1 slot
	cursor.execute("DELETE FROM offices WHERE ID='1'")
	cursor.execute("SET @i=0")
	cursor.execute("UPDATE offices SET `ID` = @i:=@i+1;")
	connection.commit()
# close the cursor object
cursor.close ()
# close the connection 
connection.close ()
sys.exit()
