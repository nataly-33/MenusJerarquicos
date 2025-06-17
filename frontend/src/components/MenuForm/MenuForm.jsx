import React, { useState } from 'react';
import axios from 'axios';
import './MenuForm.css';

function MenuForm({ onMenuAdded }) {
  const [nombre, setNombre] = useState('');

  const agregarMenu = async () => {
    if (!nombre.trim()) return;
    await axios.post('http://localhost:5000/menu', { nombre });
    setNombre('');
    onMenuAdded(); // Refresca el árbol después de agregar
  };

  return (
    <div className="menu-form">
      <input
        type="text"
        placeholder="Nombre del menú"
        value={nombre}
        onChange={e => setNombre(e.target.value)}
      />
      <button onClick={agregarMenu}>Agregar Menú</button>
    </div>
  );
}

export default MenuForm;
