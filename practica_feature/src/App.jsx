import React from 'react';
import MyButton from './components/mybutton';

function App() {
  const handleClick = () => {
    console.log('Botón clickeado!');
    alert('¡Has hecho clic en el botón!');
  };

  return (
    <div style={{ 
      display: 'flex', 
      justifyContent: 'center', 
      alignItems: 'center', 
      minHeight: '100vh',
      gap: '20px',
      flexDirection: 'column'
    }}>
      <h1>Mi Aplicación con MUI</h1>
      
      {/* Ejemplos de uso del botón */}
      <MyButton 
        label="Botón Principal" 
        onClick={handleClick}
        variant="contained"
        color="primary"
      />
      
      <MyButton 
        label="Botón Secundario" 
        onClick={handleClick}
        variant="outlined"
        color="secondary"
      />
      
      <MyButton 
        label="Botón Deshabilitado" 
        disabled={true}
        variant="contained"
        color="error"
      />
      
      <MyButton 
        label="Botón Grande" 
        onClick={handleClick}
        size="large"
        variant="contained"
        color="success"
      />
    </div>
  );
}

export default App;