
from views import db
from _config import DATABASE_PATH

import sqlite3
from datetime import datetime

with sqlite3.connect(DATABASE_PATH) as connection:

    # get a cursor object to execute SQL commands
    c = connection.cursor()

    # temporarily change the name of tasks table
    c.execute("""ALTER TABLE tasks RENAME TO old_tasks """)

    # recreate a new task table with updated schema
    db.create_all()

    # retrive data from old_task table
    c.execute("""SELECT name, due_date, priority,
            status FROM old_tasks ORDER BY task_id ASC """)

    # save all rows as a list of tuples;
    # set posted_date to now and user_id to 1
    data = [(row[0], row[1], row[2], row[3],
             datetime.now(), 1) for row in c.fetchall()]

    # insert data to task table
    c.executemany("""INSERT INTO tasks (name, due_date, priority, status,
         posted_date, user_id) VALUES (?, ?, ?, ?, ?, ?)""", data)

    # delete old_task table
    c.execute("DROP TABLE old_tasks")