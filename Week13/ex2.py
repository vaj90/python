import _sqlite3
db_str = "week13.db"
db_con = _sqlite3.connect(db_str)
cursor = db_con.cursor()

query = "select * from week12_db"
cursor.execute(query)
all_rows = cursor.fetchall()
for row in all_rows:
    print(row)
db_con.close()