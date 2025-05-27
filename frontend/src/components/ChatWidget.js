import React, { useState, useEffect } from 'react';
import io from 'socket.io-client';

const socket = io('http://localhost:3001');

function ChatWidget() {
  const [input, setInput] = useState('');
  const [chat, setChat] = useState([]);

  const sendMessage = () => {
    socket.emit('query', input);
    setChat([...chat, { user: input }]);
    setInput('');
  };

  useEffect(() => {
    socket.on('response', msg => {
      setChat(prev => [...prev, { bot: msg }]);
    });
  }, []);

  return (
    <div>
      <h3>Ask about Registrations</h3>
      {chat.map((msg, i) => (
        <div key={i}>{msg.user || msg.bot}</div>
      ))}
      <input value={input} onChange={e => setInput(e.target.value)} />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
}

export default ChatWidget;
