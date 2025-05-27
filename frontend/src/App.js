import React from 'react';
import Register from './components/Register';
import LiveRecognition from './components/LiveRecognition';
import ChatWidget from './components/ChatWidget';

function App() {
  return (
    <div>
      <h1>Face Recognition Platform</h1>
      <Register />
      <LiveRecognition />
      <ChatWidget />
    </div>
  );
}

export default App;
