import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Create the tables
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS flavors (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        is_seasonal BOOLEAN NOT NULL
    )''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY,
        ingredient TEXT NOT NULL,
        quantity INTEGER NOT NULL
    )''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS allergens (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cart (
        id INTEGER PRIMARY KEY,
        flavor_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        FOREIGN KEY(flavor_id) REFERENCES flavors(id)
    )''')


    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
