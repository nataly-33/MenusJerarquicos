import React, { useState } from 'react';
import MenuForm from '../../components/MenuForm/MenuForm';
import MenuTree from '../../components/MenuTree/MenuTree';

function HomePage() {
  const [actualizar, setActualizar] = useState(false);

  const handleInsert = () => {
    setActualizar(!actualizar);
  };

  return (
    <div>
      <MenuForm onInsert={handleInsert} />
      <MenuTree key={actualizar} />
    </div>
  );
}

export default HomePage;
