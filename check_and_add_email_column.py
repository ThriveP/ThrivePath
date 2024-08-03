import sqlite3

# Connect to your SQLite database
conn = sqlite3.connect('merodata.db')

cursor = conn.cursor()

# Check if the 'email' column exists in the 'user' table
cursor.execute("PRAGMA table_info(user);")
columns = [row[1] for row in cursor.fetchall()]

if 'email' not in columns:
    print("Adding 'email' column to 'user' table.")
    cursor.execute("ALTER TABLE user ADD COLUMN email TEXT;")
    conn.commit()
else:
    print("'email' column already exists in 'user' table.")

# Close the connection
conn.close()
