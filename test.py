from app import db
from sqlalchemy import inspect

inspector = inspect(db.engine)
tables = inspector.get_table_names()
print(tables)  # Ensure 'user' is listed
