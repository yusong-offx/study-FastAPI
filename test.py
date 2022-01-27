import psycopg2

with open("dblogin.txt") as f:
    conn = psycopg2.connect(f.read())

cur = conn.cursor()

cur.execute("SELECT * FROM movies")
data = cur.fetchall()
print(*data, sep='\n')
cur.close()
conn.close()
