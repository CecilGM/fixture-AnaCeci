from flask import Flask, jsonify, request
from flask_cors import CORS
from init_db import init_db   # Importar la función

app = Flask(__name__)
CORS(app)

DATABASE = 'worldcup.db'

def get_db():
    import sqlite3
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Endpoint para obtener todos los partidos
@app.route('/api/matches', methods=['GET'])
def get_matches():
    conn = get_db()
    matches = conn.execute('SELECT * FROM matches ORDER BY id').fetchall()
    conn.close()
    return jsonify([dict(m) for m in matches])

# Endpoint para cambiar check
@app.route('/api/matches/<int:match_id>/check', methods=['PATCH'])
def toggle_check(match_id):
    conn = get_db()
    current = conn.execute('SELECT checked FROM matches WHERE id = ?', (match_id,)).fetchone()
    if not current:
        return jsonify({'error': 'Partido no encontrado'}), 404
    new_val = 1 - current['checked']
    conn.execute('UPDATE matches SET checked = ? WHERE id = ?', (new_val, match_id))
    conn.commit()
    conn.close()
    return jsonify({'id': match_id, 'checked': new_val})

# Endpoint para resetear todo
@app.route('/api/reset', methods=['POST'])
def reset_checklist():
    conn = get_db()
    conn.execute('UPDATE matches SET checked = 0')
    conn.commit()
    conn.close()
    return jsonify({'message': 'Checklist reiniciado'}), 200

if __name__ == '__main__':
    init_db()   # Llamada para asegurar que la BD exista y tenga datos
    app.run(host='0.0.0.0', port=5000, debug=True)