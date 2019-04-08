"""
Note: This db reference needs to be updated to reflect our student/teacher data input/output


Student Table Example
+---------+----------+---------------+----------+---------+-------------------+---------------+
| id      |    tid   |  session_id   |   name   | is_lead |    midterm_done   |   final_done  |
+=========+==========+===============+==========+=========+===================+===============+
| 9228421 |   2315   |      0319     |   Mike   |  false  |       true        |     false     |
+---------+----------+---------------+----------+---------+-------------------+---------------+
"""

from datetime import date
import sqlite3
DB_FILE = 'capstone360.db'

class model():
    def __init__(self):
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute("select count(rowid) from capstone_session")
        except sqlite3.OperationalError:
            cursor.execute('CREATE TABLE capstone_session( '
                            'id INTEGER NOT NULL PRIMARY KEY, '
                            'start_term VARCHAR(10) NOT NULL, '
                            'start_year INTEGER NOT NULL, '
                            'end_term VARCHAR(10) NOT NULL, '
                            'end_year INTEGER NOT NULL);')

        try:
            cursor.execute("select count(rowid) from students")
        except sqlite3.OperationalError:
            cursor.execute('CREATE TABLE students( '
                            'id INTEGER NOT NULL, '
                            'tid INTEGER NOT NULL REFERENCES teams(id), '
                            'session_id INTEGER NOT NULL REFERENCES capstone_session(id), '
                            'name VARCHAR(128) NOT NULL, '
                            'is_lead BOOLEAN NULL DEFAULT FALSE, '
                            'midterm_done BOOLEAN NULL DEFAULT FALSE, '
                            'final_done BOOLEAN NULL DEFAULT FALSE, '
                            'PRIMARY KEY (id, session_id) );')
        try:
            cursor.execute("select count(rowid) from teams")
        except sqlite3.OperationalError:
            cursor.execute('CREATE TABLE teams( '
                            'id INTEGER NOT NULL PRIMARY KEY, '
                            'session_id INTEGER NOT NULL REFERENCES capstone_session(id), '
                            'name VARCHAR(128) NOT NULL);')

        try:
            cursor.execute("select count(rowid) from team_members")
        except sqlite3.OperationalError:
            cursor.execute('CREATE TABLE team_members( '
                            'tid INTEGER NOT NULL REFERENCES teams(id), '
                            'sid INTEGER NOT NULL REFERENCES students(id), '
                            'session_id INTEGER NOT NULL REFERENCES capstone_session(id), '
                            'PRIMARY KEY (tid, sid, session_id) );')
                            
        try:
            cursor.execute("select count(rowid) from removed_students")
        except sqlite3.OperationalError:
            cursor.execute('CREATE TABLE removed_students( '
                            'id INTEGER NOT NULL, '
                            'tid INTEGER NOT NULL REFERENCES teams(id), '
                            'session_id INTEGER NOT NULL REFERENCES capstone_session(id), '
                            'name VARCHAR(128) NOT NULL , '
                            'is_lead BOOLEAN NULL DEFAULT FALSE, '
                            'midterm_done BOOLEAN NULL DEFAULT FALSE, '
                            'final_done BOOLEAN NULL DEFAULT FALSE, '
                            'session_removed INTEGER NOT NULL REFERENCES capstone_session(id), '
                            'removed_date DATE,'
                            'PRIMARY KEY (id, session_id) );')

        cursor.close()

    def selectStudents(self):

        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students")
        return cursor.fetchall()
    
    def selectTeams(self):

        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM teams")
        return cursor.fetchall()

    def insertStudent(self, name, id, session_id, tid):
        """
        Insert data into the database
        :param name: String
        :param id: integer
        :param tid: integer
        :param session_id: integer
        """
        

        params = {'name': name, 'id': id, 'tid': tid, 'session_id': session_id, 'is_lead': 'false', 'midterm_done': 'false', 'final_done': 'false'}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into students (id, tid, session_id, name, is_lead, midterm_done, final_done) VALUES (:id, :tid, :session_id, :name, :is_lead, :midterm_done, :final_done)", params)
        connection.commit()
        cursor.close()
        return True

    def insertTeam(self, id, session_id, name):

        params = {'id': id, 'session_id': session_id, 'name': name, }
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into teams (id, session_id, name) VALUES (:id, :session_id, :name)", params)
        connection.commit()
        cursor.close()
        return True

    def removeStudent(self, id, session_id):
        
        params = {'id': id, 'session_id': session_id}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("delete from students where id = :id AND session_id = :session_id", params)
        connection.commit()
        cursor.close()
        return True

    def removeTeam(self, id, session_id):
        
        params = {'id': id, 'session_id': session_id}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("delete from students where tid = :id AND session_id = :session_id", params)
        cursor.execute("delete from teams where id = :id AND session_id = :session_id", params)
        connection.commit()
        cursor.close()
        return True