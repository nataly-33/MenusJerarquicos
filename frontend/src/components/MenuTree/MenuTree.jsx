import React from 'react';
import './MenuTree.css';

function Nodo({ nodo }) {
  if (!nodo || nodo.claves.length === 0) return null;

  return (
    <ul className="nodo">
      <li>
        {nodo.claves.join(", ")}
        {nodo.hijos && nodo.hijos.some(h => h !== null) && (
          <ul>
            {nodo.hijos.map((hijo, index) =>
              hijo ? <Nodo key={index} nodo={hijo} /> : null
            )}
          </ul>
        )}
      </li>
    </ul>
  );
}

function MenuTree({ arbol }) {
  return (
    <div className="menu-tree">
      {arbol && arbol.claves.length > 0 ? (
        <Nodo nodo={arbol} />
      ) : (
        <p>No hay menús disponibles.</p>
      )}
    </div>
  );
}

export default MenuTree;
