import React from 'react';
import './PantallaCarga.css';

const LoadingScreen = () => {
    return (
        <div className="loading-container">
            <div className="spinner"></div>
            <p>Cargando...</p>
        </div>
    );
};

export default LoadingScreen;
