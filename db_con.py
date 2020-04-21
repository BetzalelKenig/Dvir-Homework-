import psycopg2 as pg2
import os

con = pg2.connect(database="test",
                       host="localhost",
                       user="postgres",
                       port="5432",
                       password=os.environ.get('DB_PASS')
                       )

cur = con.cursor()

cur.execute("""SELECT * FROM person 
	WHERE CHAR_LENGTH(password) > 10 
	ORDER BY city""")

rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()

con.close()



