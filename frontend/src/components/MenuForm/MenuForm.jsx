import React, { useState } from 'react';
import axios from 'axios';
import './MenuForm.css';

function MenuForm({ onInsert }) {
  const [dato, setDato] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!dato) return;

    try {
      await axios.post('http://localhost:5000/insertar', { dato }); 
      onInsert(); 
      setDato(''); 
    } catch (error) {
      console.error('Error al insertar', error);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="menu-form">
      <input
        type="text"
        placeholder="Ingrese dato del menú"
        value={dato}
        onChange={(e) => setDato(e.target.value)}
      />
      <button type="submit">Insertar</button>
    </form>
  );
}

export default MenuForm;
