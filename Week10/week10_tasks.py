import sqlite3
from sqlite3 import Error


def create_db(db_path):
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except Error as e:
        print("Some error occurred,", e.args[0])
    return conn


def db_execute(db_con, query, task=None):
    try:
        db_cursor = db_con.cursor()
        if task is None:
            db_cursor.execute(query)
        else:
            db_cursor.execute(query, task)
        db_con.commit()
        return db_cursor
    except Exception as e:
        print("Some error occurred,", e.args)


db_str = 'student.db'

student_table = """ CREATE TABLE IF NOT EXISTS students (
        student_id integer,
        name text NOT NULL,
        PRIMARY KEY (student_id)
    );"""

course_table = """ CREATE TABLE IF NOT EXISTS courses (
        course_code text,
        course_name text NOT NULL,
        PRIMARY KEY (course_code)
    );"""

grade_table = """ CREATE TABLE IF NOT EXISTS grades (
        student_id integer NOT NULL,
        course_code text NOT NULL,
        grade_percent integer NOT NULL,
        PRIMARY KEY (student_id, course_code),
        FOREIGN KEY (student_id) REFERENCES students (student_id) 
            ON DELETE CASCADE ON UPDATE NO ACTION,
        FOREIGN KEY (course_code) REFERENCES courses (course_code) 
            ON DELETE CASCADE ON UPDATE NO ACTION
    );"""

# select query
select_students = "select * from students"
select_courses = "select * from courses"
select_grades = "select * from grades"

# select by key query
select_student_by_id = "select from students where student_id={:d}"
select_course_by_course_code = "select from courses where course_code='{:s}'"
select_grade_by_student_id = "select from grades where student_id={:d}"
select_grade_by_course_code = "select from grades where course_code='{:s}'"

# delete query
delete_student_by_id = "delete from students where student_id={:d}"
delete_course_by_course_code = "delete from courses where course_code='{:s}'"
delete_grade_by_student_id = "delete from grades where student_id={:d}"

# insert data query
insert_student = "INSERT INTO students (student_id,name) VALUES ({:d},'{:s}')"
insert_course = "INSERT INTO courses (course_code,course_name) VALUES(?,?)"
insert_grades = "INSERT INTO grades (student_id,course_code,grade_percent) VALUES(?,?,?);"

# update query
update_student = """
    UPDATE students set 
        student_id = ?,
        name = ?
    WHERE student_id = ?
"""
update_course = """
    UPDATE courses set 
        course_code = ?,
        course_name = ?
    WHERE course_code = ?
"""
update_grade = """
    UPDATE grades set 
        grade_percent = ?
    WHERE student_id = ?
"""

# dummy data
students = [
    [101285226, "Allan John Valiente"],
    [101285227, "Peter Parker"],
    [101285228, "Tony Stark"],
    [101285229, "Clark Kent"],
    [101285230, "Bruce Wayne"]
]
courses = [
    ("COMP 2080", "DATA STRUCTURES & ALGORITHMS"),
    ("COMP 2139", "WEB APPLICATION DEVELOPMENT"),
    ("COMP 2148", "PROFESSIONAL WORKPLACE COMPETITION"),
    ("COMP 2151", "AGILE SOFTWARE DEVELOPMENT"),
    ("COMP 2152", "OPEN SOURCE DEVELOPMENT")
]
grades = [
    (101285226, "COMP 2080", 88),
    (101285226, "COMP 2139", 90),
    (101285229, "COMP 2148", 96),
    (101285228, "COMP 2151", 92),
    (101285230, "COMP 2152", 89)
]
db = create_db(db_str)

# Task 1
# -Create a new sqlite database file
# -Create the following tables in the database above
"""
students
    student_id
    name

courses
    course_code
    course_name

grades
    student_id
    course_code
    grade_percent
"""
print("\nTask 1")
if db is not None:
    db_execute(db, student_table)
    db_execute(db, course_table)
    db_execute(db, grade_table)
    print("tables are created")
else:
    print("Error! cannot create the database connection.")

# Task 2
# -Choose one table and output the column names and data types
print("\nTask 2")
if db is not None:
    data = db_execute(db, "PRAGMA table_info(students)")
    rows = data.fetchall()
    disp = "{0:20s}\t{1:s}"
    print(disp.format("column", "data type"))
    for r in rows:
        column_name = r[1]
        data_type = r[2]
        print(disp.format(column_name, data_type))

# Task 3
# -Insert 5 rows into the students table using String formatting
print("\nTask 3")
if db is not None:
    for s in students:
        db_execute(db, insert_student.format(s[0], s[1]))
    print("Student records successfully added")

# Task 4
# -Insert 5 rows into the courses table, passing parameters to the execute() method
print("\nTask 4")
if db is not None:
    for c in courses:
        db_execute(db, insert_course, c)
    print("Courses successfully added")

# Task 5
# -Insert 5 rows into the grades table using any method
print("\nTask 5")
if db is not None:
    for g in grades:
        db_execute(db, insert_grades, g)
    print("Grades successfully added")

# Task 6
# -Remove 1 row from each table
print("\nTask 6")
if db is not None:
    db_execute(db, delete_student_by_id.format(101285230))
    print("student successfully deleted")

    db_execute(db, delete_course_by_course_code.format("COMP 2152"))
    print("course successfully deleted")

    db_execute(db, delete_grade_by_student_id.format(101285230))
    print("grade successfully deleted")

# Task 7
# -Update 1 row from each table
print("\nTask 7")
if db is not None:
    db_execute(db, update_student, (101285226, "Allan Valiente", 101285226))
    print("student successfully updated")

    db_execute(db, update_course, ("COMP 2080", "DATA STRUCTURES & ALGORITHMS", "COMP 2080"))
    print("course successfully updated")

    db_execute(db, update_grade, (90, 101285226))
    print("student successfully updated")

# Task 8
# -Retrieve all rows from the students table. Use the row factory to display the data
print("\nTask 8")
if db is not None:
    student_record = db_execute(db, select_students)
    rows = student_record.fetchall()
    for r in rows:
        print(r)

# Task 9
# -The first three rows from the courses table. Use the row factory to display just the course name
print("\nTask 9")
if db is not None:
    course_record = db_execute(db, "select * from courses limit 3")
    rows = course_record.fetchall()
    for r in rows:
        print(r[1])

# Task 10
# -Delete any table created in Task 1
print("\nTask 10")
if db is not None:
    db_execute(db, "DROP TABLE grades")
    print("Grade table successfully deleted")
