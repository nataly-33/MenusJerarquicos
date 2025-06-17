import React, { useEffect, useState } from 'react';
import axios from 'axios';
import MenuForm from '../../components/MenuForm/MenuForm';
import MenuTree from '../../components/MenuTree/MenuTree';
import './HomePage.css';

function HomePage() {
  const [arbol, setArbol] = useState(null);

  const fetchMenu = async () => {
    const res = await axios.get('http://localhost:5000/menu');
    setArbol(res.data);
  };

  useEffect(() => {
    fetchMenu();
  }, []);

  return (
    <div className="home-page">
      <h2>Sistema de Menús Jerárquicos</h2>
      <MenuForm onMenuAdded={fetchMenu} />
      <MenuTree arbol={arbol} />
    </div>
  );
}

export default HomePage;
