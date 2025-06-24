import React, { useEffect, useState } from 'react';
import axios from 'axios';
import LoadingScreen from '../PantallaCarga/PantallaCarga';
import './MenuTree.css';

const MenuTree = () => {
    const [niveles, setNiveles] = useState({});
    const [cargando, setCargando] = useState(false);

    useEffect(() => {
        fetchNiveles();
    }, []);

    const fetchNiveles = async () => {
        try {
            setCargando(true);
            const response = await axios.get('http://localhost:5000/listar');
            setNiveles(response.data);
            console.log("Arbol", response.data);

        } catch (error) {
            console.error('Error al obtener niveles', error);
        } finally {
            setCargando(false);
        }
    };

    const renderNiveles = () => {
        return Object.entries(niveles).map(([nivel, nodos], index) => (
            <div key={index} className="nivel-container">
                <h3>Nivel {nivel}</h3>
                <div className="nodo-container">
                    {nodos.map((nodo, i) => (
                        <div key={i} className="nodo">
                            {' | |  '+nodo.join(' | |  ')+' | |  '}
                        </div>
                    ))}
                </div>
            </div>
        ));
    };

    return (
        <div>
            {cargando && <LoadingScreen />}
            {!cargando && renderNiveles()}
        </div>
    );
};

export default MenuTree; 
/*
1	Configuración General	null
1.1	Fecha y Hora	1
1.2	Idioma	1
1.3	Actualizaciones	1
2	Hardware	null
2.1	Teclado	2
2.2	Pantalla	2
2.3	Red	2
2.3.1	Wi-Fi	2.3
2.3.2	Ethernet	2.3
2.4	Impresora	2
3	Software	null
3.1	Aplicaciones	3
3.2	Permisos	3
3.3	Seguridad	3
3.3.1	Antivirus	3.3
3.3.2	Firewall	3.3
4	Usuarios	null
4.1	Crear Usuario	4
4.2	Eliminar Usuario	4
4.3	Cambiar Contraseña	4


*/