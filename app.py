import socketio

sio = socketio.AsyncServer(async_mode='asgi')
app = socketio.ASGIApp(sio, static_files={
    '/': './public/'
})
import json

@sio.event
def connect(sid, environ):
    print(sid, 'connected')


@sio.event
def disconnect(sid):
    print(sid, 'disconnected')


@sio.event
async def message(sid, data):
    print(sid, data)
    await sio.emit('awesome', {"data": f"data sent from frontend is {data}"}, to=sid) # room can also be used here instead of to


