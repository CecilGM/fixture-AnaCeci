from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
from datos_partidos import PARTIDOS

app = Flask(__name__)
CORS(app)

def init_db():
    conn = sqlite3.connect('mundial.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS partidos (
            id INTEGER PRIMARY KEY,
            grupo TEXT,
            local TEXT,
            visitante TEXT,
            fecha TEXT,
            hora TEXT,
            estadio TEXT,
            visto INTEGER DEFAULT 0
        )
    ''')
    
    cursor.execute("SELECT COUNT(*) FROM partidos")
    if cursor.fetchone()[0] == 0:
        for p in PARTIDOS:
            cursor.execute('INSERT INTO partidos VALUES (?,?,?,?,?,?,?,?)', 
                         (p['id'], p['grupo'], p['local'], p['visitante'], 
                          p['fecha'], p['hora'], p['estadio'], p['visto']))
        conn.commit()
        print("✅ Base de datos creada")
    conn.close()

@app.route('/api/partidos', methods=['GET'])
def get_partidos():
    conn = sqlite3.connect('mundial.db')
    conn.row_factory = sqlite3.Row
    partidos = conn.execute('SELECT * FROM partidos ORDER BY id').fetchall()
    conn.close()
    return jsonify([dict(p) for p in partidos])

@app.route('/api/partidos/<int:id>/marcar', methods=['PATCH'])
def marcar(id):
    conn = sqlite3.connect('mundial.db')
    actual = conn.execute('SELECT visto FROM partidos WHERE id = ?', (id,)).fetchone()
    nuevo = 1 - actual[0]
    conn.execute('UPDATE partidos SET visto = ? WHERE id = ?', (nuevo, id))
    conn.commit()
    conn.close()
    return jsonify({'id': id, 'visto': nuevo})

@app.route('/api/reiniciar', methods=['POST'])
def reiniciar():
    conn = sqlite3.connect('mundial.db')
    conn.execute('UPDATE partidos SET visto = 0')
    conn.commit()
    conn.close()
    return jsonify({'mensaje': 'Lista reiniciada'})

if __name__ == '__main__':
    init_db()
    app.run(port=5000)