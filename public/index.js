const sio = io();

sio.on('connect', () => {
  console.log('connected');
  sio.emit('message', {"number": "1"}, (data) => {
    console.log(data);
  });
});

sio.on('disconnect', () => {
  console.log('disconnected');
});

sio.on('awesome', (data) => {
  console.log(data);
});
