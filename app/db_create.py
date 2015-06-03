# db_create.py

from views import db
from models import Task
from datetime import date

# create the database and the table
db.create_all()

# instert data
db.session.add(Task("Finish this tutorial", date(2015, 3, 13), 10, 1))
db.session.add(Task("Finish Real Pyhton", date(2015, 3, 13), 10, 1))

# commit the changes
db.session.commit()