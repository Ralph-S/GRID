import React, { useEffect, useState } from 'react';
import CamThermalToggle from './CamThermalToggle';

function LiveFeed() {

    const [imageSrc, setImageSrc] = useState('');

    useEffect(() => {
        const fetchImage = () => {
            fetch('http://localhost:5000/latest-image')
                .then(response => response.blob())
                .then(blob => {
                    const url = URL.createObjectURL(blob);
                    setImageSrc(url);
                })
                .catch(error => console.error('Error fetching the latest image:', error));
        };

        fetchImage();
        const interval = setInterval(fetchImage, 1000);

        return () => clearInterval(interval);
    }, []);

    return (
        <div className="live-feed">
            <h2>Live feed from UGV</h2>
            {imageSrc ? <img src={imageSrc} alt="Live Feed" style={{ width: '100%' }} /> : 'Loading...'}
        </div>
    );

    // return (
    //     <div className="live-feed">
    //         <h2>Live feed from UGV</h2>
    //         Placeholder for live feed
    //         <CamThermalToggle />
    //     </div>
    // );
}

export default LiveFeed;