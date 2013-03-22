import sqlite3

DB = None
CONN = None


def make_new_student(first_name, last_name, github):
    query = """INSERT into Students values (?, ?, ?)"""
    DB.execute(query, (first_name, last_name, github))
    CONN.commit()
    print """Successfully added student: %s %s"""%(first_name, last_name)

def make_new_project(title, description, max_grade):
    query = """INSERT into Projects VALUES (?, ?, ?) """
    DB.execute(query, (title, description, max_grade))
    CONN.commit()
    print """Successfully added project %s"""%(title)

def give_grade(student_github, project_title, grade):
    query = """INSERT into Grades values (?, ?, ?)"""
    DB.execute(query, (student_github, project_title, grade))
    CONN.commit()
    print """Successfully added grade: %s""" %(grade)

def student_grade(student_github, project_title):
    query = """SELECT grade FROM Grades WHERE student_github=? AND project_title=?"""
    DB.execute(query, (student_github, project_title))
    row = DB.fetchone()
    print """Grade: %s"""%(row)

def student_grades(first_name):
    query = """SELECT first_name, project_title, grade FROM ReportCardView WHERE first_name=?"""
    DB.execute(query, (first_name))
    row = DB.fetchone()
    print """%s has %s for %s"""%(row[0],row[2],row[1])

def get_student_by_github(github):
    query = """SELECT first_name, last_name, github FROM Students WHERE github = ?"""
    DB.execute(query, (github,))
    row = DB.fetchone()
    print """\
Student: %s %s
Github account: %s"""%(row[0], row[1], row[2])

def list_project(name):
    query = """SELECT * FROM Projects WHERE title = ?"""
    DB.execute(query, (name,))
    row = DB.fetchone()
    print"""\
    Project: %s 
    Max Score: %s """ %(row[0], row[2])

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("my_database.db")
    DB = CONN.cursor()

def main():
    connect_to_db()
    command = None
    while command != "quit":
        input_string = raw_input("HBA Database > ")
        tokens = input_string.split(", ")
        command = tokens[0]
        args = tokens[1:]

        if command == "student":
            get_student_by_github(*args) 
        elif command == "new_student":
            make_new_student(*args)
        elif command == "project_title":
            list_project(*args)
        elif command == "new_project":
            make_new_project(*args)
        elif command == "get_grade":
            student_grade(*args)
        elif command == "give_grade":
            give_grade(*args)
        elif command == "student_grades":
            student_grades(*args)
        
    CONN.close()


if __name__ == "__main__":
    main()
