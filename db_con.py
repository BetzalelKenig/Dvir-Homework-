import psycopg2
import os

con = psycopg2.connect(database="test",
                       host="localhost",
                       user="postgres",
                       port="5432",
                       password=os.environ.get('DB_PASS')
                       )

cur = con.cursor()

cur.execute("select * from person")

rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()

con.close()


