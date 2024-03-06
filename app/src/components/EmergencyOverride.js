import React from 'react';

const EmergencyOverride = () => {
  const handleEmergency = () => {
    fetch('http://localhost:5000/emergency-override', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({emergency: true}),
    })
    .then(response => response.json())
    .then(data => {
      console.log('Success:', data);
    })
    .catch((error) => {
      console.error('Error:', error);
    });
  };

  return (
    <div className="component emergency-override">
      <button className='round-button' onClick={handleEmergency}>
        <div>Emergency</div>
        <div>Override</div>
      </button>
    </div>
  );
};

export default EmergencyOverride;
