import React, { useState } from 'react';
import './styles/App.css';
import LiveFeed from './components/LiveFeed';
import MapDisplay from './components/MapDisplay';
import SensorData from './components/SensorData';
import OdometryData from './components/OdometryData';
import TerminalLogger from './components/TerminalLogger';
import EmergencyOverride from './components/EmergencyOverride';

function App() {
  const [isEmergency, setIsEmergency] = useState(false);
  console.log("Is emergency:", isEmergency);
  return (
    <div className="app">
      <div className="grid-container" style={{ backgroundColor: isEmergency ? '#ec8989' : '#74aa72' }}>
        <p className='name'>GRID</p>
        <LiveFeed className="live-feed comp"/>
        <MapDisplay className="map-display comp"/>
        <SensorData className="sensor-data comp"/>
        <OdometryData className="odometry-data comp"/>
        <EmergencyOverride isEmergency={isEmergency} setIsEmergency={setIsEmergency} className="emergency-override comp1"/>
        <TerminalLogger className="terminal-logger comp"/>
      </div>
    </div>
  );
}

export default App;