import _sqlite3
from contextlib import closing

db_str = "movies.sqlite"


def print_query(cs, q):
    cs.execute(q)
    result_set = cs.fetchall()
    for row in result_set:
        print(row)
    print()


conn = _sqlite3.connect(db_str)
c = conn.cursor()

print("A SELECT statement that gets the content of all columns ")
print_query(c, '''SELECT * FROM Movie''')

print("A SELECT statement that gets the selected columns and rows")
print_query(c, '''SELECT name, minutes FROM Movie WHERE minutes < 90 ORDER BY minutes ASC''')

print("A SELECT statement that gets the data from two tables - related")
print_query(c, '''SELECT Movie.name, Category.name as CategoryName, minutes from Movie
 JOIN Category ON Category.categoryID = Movie.categoryID
 WHERE minutes < 95
  ORDER BY minutes ASC''')

print("An INSERT statement ")
# c.execute('''INSERT INTO Movie (name, year, minutes, categoryID) VALUES  ('JUno 2021', 2007, 96, 2)''')
# print("A SELECT that gets the content of all columns")
# print_query(c, '''SELECT * FROM Movie''')

print("An Update Statement")
print_query(c, '''Update Movie SET minutes == 200 WHERE movieID = 4''')
print("A SELECT statement that gets the content of all columns ")
print_query(c, '''SELECT * FROM Movie''')

print("An DELETE Statement")
c.execute('''DELETE FROM Movie where year = 2004''')
print("A SELECT statement that gets the content of all columns ")
print_query(c, '''SELECT * FROM Movie''')

print("How to execute statement with a parameter")
query = '''SELECT * FROM Movie WHERE minutes < ?'''
c.execute(query, (90,))
out = c.fetchall()
for line in out:
    print(line)
print()

conn.row_factory = _sqlite3.Row
with closing(conn.cursor()) as c:
    query = '''SELECT * FROM Movie WHERE MINUTES < ?'''
    c.execute(query, (120,))
    movies = c.fetchall()

for movie in movies:
    print(movie["name"], "|", movie["year"], "|", movie["minutes"])

name = "Avatar"
year = 2008
minutes = 146
categoryID = 2
with closing(conn.cursor()) as c:
    query = '''INSERT INTO Movie (name,year,minutes,categoryID) VALUES(?,?,?,?)'''
    c.execute(query, (name, year, minutes, categoryID))
    conn.commit()

conn = _sqlite3.connect(db_str)
c = conn.cursor()

print("A SELECT statement that gets the content of all columns ")
print_query(c, '''SELECT * FROM Movie''')

id = 4
minutes = 84
with closing(conn.cursor()) as c:
    query = '''Update Movie SET minutes == ? WHERE movieID = ?'''
    c.execute(query, (minutes, id))
    conn.commit()

conn = _sqlite3.connect(db_str)
c = conn.cursor()

print("A SELECT statement that gets the content of all columns ")
print_query(c, '''SELECT * FROM Movie''')

id = 10
with closing(conn.cursor()) as c:
    query = '''DELETE FROM Movie where movieID = ?'''
    c.execute(query, (id,))
    conn.commit()

conn = _sqlite3.connect(db_str)
c = conn.cursor()

print("A SELECT statement that gets the content of all columns ")
print_query(c, '''SELECT * FROM Movie''')

