import React, { useState } from 'react';

const EmergencyOverride = ({ isEmergency, setIsEmergency }) => {
  const [buttonText, setButtonText] = useState('Emergency Override');

  const handleEmergency = () => {
    const newState = buttonText === 'Emergency Override' ? 'Automated Mode' : 'Emergency Override';

    fetch('http://localhost:5000/emergency-override', { 
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ state: newState }), 
    })
    .then(response => response.json())
    .then(data => {
      console.log('Success:', data);
      setButtonText(newState);
      setIsEmergency(!isEmergency);
    })
    .catch((error) => {
      console.error('Error:', error);
    });
  };

  return (
    <div className="component emergency-override">
      <button className='round-button' onClick={handleEmergency}>
        <div>{buttonText}</div>
      </button>
    </div>
  );
};

export default EmergencyOverride;
