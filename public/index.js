const sio = io();

sio.on('connect', () => {
  console.log('connected');
  sio.emit('message', {"number": "1"});
});

sio.on('disconnect', () => {
  console.log('disconnected');
});

