import React, { useState } from 'react';

const CamThermalToggle = () => {
    const [mode, setMode] = useState('CAM'); // Initial mode

    const handleClick = (newMode) => {
        setMode(newMode);
    };

    return (
        <div className="buttons">
            <button 
                onClick={() => handleClick('CAM')} 
                style={{ backgroundColor: mode === 'CAM' ? 'blue' : 'gray', color: 'white' }}
                disabled={mode === 'CAM'}
            >
                CAM
            </button>
            <button 
                onClick={() => handleClick('Thermal')} 
                style={{ backgroundColor: mode === 'Thermal' ? 'blue' : 'gray', color: 'white' }}
                disabled={mode === 'Thermal'}
            >
                Thermal
            </button>
        </div>
    );
};

export default CamThermalToggle;
