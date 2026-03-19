import sqlite3

conn = sqlite3.connect("emotions.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM emotion_records")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()