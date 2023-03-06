import sqlite3
from sqlite3 import Error

def create_connection(db_file):
   """ create a database connection to the SQLite database """
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       return conn
   except Error as e:
       print(e)
   return conn

def execute_sql(conn, sql):
   """ Execute sql """
   try:
       c = conn.cursor()
       c.execute(sql)
   except Error as e:
       print(e)

def add_data(conn):
    task = (1, "The Great Gatsby", "F.Scott Fitzgerald", 1896, 3)
    sql = '''INSERT INTO books(id, title, author, year_of_publishing, amount)
             VALUES(?, ?, ?, ?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid

if __name__ == "__main__":
    create_books_table_sql = """
    CREATE TABLE IF NOT EXISTS books (
        id integer PRIMARY KEY,
        title text NOT NULL,
        author text NOT NULL,
        year_of_publishing integer NOT NULL,
        amount integer NOT NULL
    );
    """

    db_file = "databasebooks.db"

    conn = create_connection(db_file)
    if conn is not None:
        execute_sql(conn, create_books_table_sql)
        add_data(conn)
    else:
        print("Error")

    # Close connection
    conn.close()