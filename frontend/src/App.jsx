import React, { useState, useEffect } from 'react';

function App() {
  const [partidos, setPartidos] = useState([]);
  const [cargando, setCargando] = useState(true);

  useEffect(() => {
    fetch('http://localhost:5000/api/partidos')
      .then(res => res.json())
      .then(data => {
        setPartidos(data);
        setCargando(false);
      });
  }, []);

  const marcar = async (id) => {
    const res = await fetch(`http://localhost:5000/api/partidos/${id}/marcar`, { method: 'PATCH' });
    const data = await res.json();
    setPartidos(partidos.map(p => p.id === id ? { ...p, visto: data.visto } : p));
  };

  const reiniciar = async () => {
    await fetch('http://localhost:5000/api/reiniciar', { method: 'POST' });
    const res = await fetch('http://localhost:5000/api/partidos');
    const data = await res.json();
    setPartidos(data);
  };

  if (cargando) return <h2>Cargando...</h2>;

  const vistos = partidos.filter(p => p.visto === 1).length;

  return (
    <div style={{ padding: 20 }}>
      <h1>🌍 Mundial 2026</h1>
      <p>Progreso: {vistos} de {partidos.length}</p>
      <button onClick={reiniciar}>Reiniciar</button>
      {partidos.map(p => (
        <div key={p.id} style={{ border: '1px solid #ccc', margin: 10, padding: 10 }}>
          <h3>{p.local} vs {p.visitante}</h3>
          <p>{p.fecha} - {p.hora}</p>
          <button onClick={() => marcar(p.id)}>
            {p.visto === 1 ? '✓ Visto' : '☐ Marcar'}
          </button>
        </div>
      ))}
    </div>
  );
}

export default App;