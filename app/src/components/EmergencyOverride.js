import React, { useState } from 'react';

const EmergencyOverride = ({ isEmergency, setIsEmergency }) => {
  const [buttonText, setButtonText] = useState('Enter Emergency Mode');

  const handleEmergency = () => {
    const newState = buttonText === 'Enter Emergency Mode' ? 'Exit Emergency Mode' : 'Enter Emergency Mode';
  
    fetch('http://localhost:5000/emergency-override', { 
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ state: newState === 'Enter Emergency Mode' ? 'Automated Mode' : 'Emergency Override' }), 
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
