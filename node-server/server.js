const express = require('express');
const http = require('http');
const { Server } = require('socket.io');
const { spawn } = require('child_process');

const app = express();
const server = http.createServer(app);
const io = new Server(server);

io.on('connection', socket => {
  console.log('Client connected');

  socket.on('query', question => {
    const py = spawn('python3', ['backend/query_rag.py', question]);
    py.stdout.on('data', data => {
      socket.emit('response', data.toString());
    });
  });
});

server.listen(3001, () => console.log('Socket server running on port 3001'));
