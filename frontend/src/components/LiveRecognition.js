import React, { useRef, useEffect } from 'react';

function LiveRecognition() {
  const videoRef = useRef();

  useEffect(() => {
    navigator.mediaDevices.getUserMedia({ video: true }).then(stream => {
      videoRef.current.srcObject = stream;
    });
  }, []);

  return (
    <div>
      <h3>Live Recognition</h3>
      <video ref={videoRef} autoPlay width="640" height="480" />
    </div>
  );
}

export default LiveRecognition;
