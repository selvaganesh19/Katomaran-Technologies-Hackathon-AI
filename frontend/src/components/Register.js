import React, { useRef, useEffect } from 'react';
import axios from 'axios';

function Register() {
  const videoRef = useRef(null);
  const nameRef = useRef();

  useEffect(() => {
    navigator.mediaDevices.getUserMedia({ video: true }).then(stream => {
      videoRef.current.srcObject = stream;
    });
  }, []);

  const captureAndRegister = async () => {
    const canvas = document.createElement('canvas');
    canvas.width = 640;
    canvas.height = 480;
    const ctx = canvas.getContext('2d');
    ctx.drawImage(videoRef.current, 0, 0);
    const base64 = canvas.toDataURL('image/jpeg').split(',')[1];

    await axios.post('http://localhost:5000/register', {
      image: base64,
      name: nameRef.current.value
    });
  };

  return (
    <div>
      <h3>Register Face</h3>
      <video ref={videoRef} autoPlay width="640" height="480" />
      <input ref={nameRef} placeholder="Enter Name" />
      <button onClick={captureAndRegister}>Register</button>
    </div>
  );
}

export default Register;
