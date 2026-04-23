import sqlite3
import json
import os

DATABASE = 'worldcup.db'
JSON_DATA = 'fixture.json'

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS matches (
            id INTEGER PRIMARY KEY,
            stage TEXT,
            home TEXT,
            away TEXT,
            date TEXT,
            time TEXT,
            venue TEXT,
            checked INTEGER DEFAULT 0
        )
    ''')
    
    cursor.execute('SELECT COUNT(*) FROM matches')
    count = cursor.fetchone()[0]
    
    if count == 0:
        
        if not os.path.exists(JSON_DATA):
            print(f"❌ No se encuentra el archivo {JSON_DATA}")
            conn.close()
            return
        
        with open(JSON_DATA, 'r', encoding='utf-8') as f:
            matches = json.load(f)
        
        for match in matches:
            cursor.execute('''
                INSERT INTO matches (id, stage, home, away, date, time, venue, checked)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (match['id'], match['stage'], match['home'], match['away'],
                  match['date'], match['time'], match['venue'], match['checked']))
        
        conn.commit()
        print(f"✅ Base de datos inicializada con {len(matches)} partidos.")
    else:
        print(f"ℹ️ La base de datos ya contiene {count} partidos. No se modificó.")
    
    conn.close()

if __name__ == '__main__':
    init_db()