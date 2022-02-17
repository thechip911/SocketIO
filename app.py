import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': './public/'
})
import json

@sio.event
def connect(sid, environ):
    print(sid, 'connected')


@sio.event
def disconnect(sid):
    print(sid, 'disconnected')


@sio.on('my_event', namespace='/chat')
def my_event(sid, data):
    print(data)
    sio.emit('my response', data, room=sid)
