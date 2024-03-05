import React from 'react';
import './App.css';
import LiveFeed from './components/LiveFeed';
import MapDisplay from './components/MapDisplay';
import SensorData from './components/SensorData';
import OdometryData from './components/OdometryData';
import TerminalLogger from './components/TerminalLogger';
import EmergencyOverride from './components/EmergencyOverride';

function App() {
  return (
    <div className="app">
      <div className="grid-container">
        <p className='name'>GRID</p>
        <LiveFeed className="live-feed comp"/>
        <MapDisplay className="map-display comp"/>
        <SensorData className="sensor-data comp"/>
        <OdometryData className="odometry-data comp"/>
        <EmergencyOverride className="emergency-override comp1"/>
        <TerminalLogger className="terminal-logger comp"/>
      </div>
    </div>
  );
}

export default App;