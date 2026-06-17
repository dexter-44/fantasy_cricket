import sqlite3
import os

DB_NAME = 'players.db'

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_database():
    """Initialize database with tables and sample data"""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Create stats table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS stats (
        player TEXT PRIMARY KEY,
        matches INTEGER,
        runs INTEGER,
        "100s" INTEGER,
        "50s" INTEGER,
        value INTEGER,
        ctg TEXT
    )''')
    
    # Create teams table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS teams (
        name TEXT PRIMARY KEY,
        players TEXT,
        value INTEGER DEFAULT 0
    )''')
    
    # Create match table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS match (
        player TEXT PRIMARY KEY,
        scored INTEGER DEFAULT 0,
        faced INTEGER DEFAULT 0,
        fours INTEGER DEFAULT 0,
        sixes INTEGER DEFAULT 0,
        bowled INTEGER DEFAULT 0,
        maiden INTEGER DEFAULT 0,
        given INTEGER DEFAULT 0,
        wkts INTEGER DEFAULT 0,
        catches INTEGER DEFAULT 0,
        stumping INTEGER DEFAULT 0,
        ro INTEGER DEFAULT 0
    )''')
    
    # Sample player data
    stats_data = [
        ('Virat Kohli', 199, 8257, 29, 43, 120, 'BAT'),
        ('Yuvraj', 86, 3589, 10, 21, 100, 'BAT'),
        ('Rohane', 158, 5435, 11, 31, 85, 'BAT'),
        ('Dhawan', 25, 565, 2, 1, 85, 'AR'),
        ('Dhoni', 78, 2573, 3, 19, 75, 'BAT'),
        ('Axar', 67, 208, 0, 0, 100, 'BWL'),
        ('Pandya', 70, 77, 0, 0, 75, 'BWL'),
        ('Jadeja', 116, 675, 0, 0, 85, 'BWL'),
        ('Kedar', 111, 1914, 6, 10, 90, 'AR'),
        ('Ashwin', 296, 1914, 10, 64, 110, 'AR'),
        ('Umesh', 73, 1365, 0, 8, 60, 'BWL'),
        ('Bumrah', 17, 289, 0, 2, 75, 'BWL'),
        ('Bhuvneshwar', 304, 8701, 14, 52, 85, 'BAT'),
        ('Rohit', 11, 111, 0, 0, 75, 'AR'),
        ('Karthik', 11, 111, 0, 0, 75, 'AR')
    ]
    
    cursor.executemany('''
        INSERT OR REPLACE INTO stats 
        (player, matches, runs, "100s", "50s", value, ctg) 
        VALUES (?,?,?,?,?,?,?)
    ''', stats_data)
    
    conn.commit()
    conn.close()
    print("✅ Database initialized successfully!")

if __name__ == "__main__":
    init_database()