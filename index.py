\#!/usr/bin/python

# Turn on debug mode.
import cgitb
import cgi
import time

cgitb.enable()

# Print necessary headers.
print("Content-Type: text/html")

# Connect to the database.
import pymysql
conn = pymysql.connect(
    db='example',
    user='root',
    passwd='ngiseD16',
    host='localhost')
c = conn.cursor()

# Insert some example data.
#c.execute("UPDATE tictactoe SET player='o' WHERE player='x';")
#conn.commit()
#c.execute("UPDATE tictactoe SET player='o' WHERE player='x';")
#conn.commit()
c.execute("UPDATE tictactoe SET player='blank' WHERE player=' ';")

conn.commit()

# Print the contents of the database.
c.execute("SELECT * FROM tictactoe")
#print("<button type=\"button\">Hello</button>")

#form = cgi.FieldStorage()

print([(r[0], r[1], r[2]) for r in c.fetchall()])
#print("<br/>")
print("<form action=\"index.py\">")
print("<textarea name=\"textinput\">This is the value</textarea>")
print("<button type=\"submit\">Submit</button>")
print("</form>")

#for key in sorted(form.keys())
#	print(key)
#        c.execute("INSERT INTO ")
#	conn.commit()
#print("<input type=\"text\" />")
#print("<button type=\"button\">GO</button>")
