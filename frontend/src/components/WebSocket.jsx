import React, { Component } from 'react';
import socketIOClient from 'socket.io-client';

const namespace = '/test';
let socket;

class WebSocket extends Component {
  constructor() {
    super();
    this.state = {
      response: false,
    };
  }

  componentDidMount() {
    socket = socketIOClient(namespace);
    socket.on('connect', data => {
      console.log('socket connected');
      socket.emit('custom_connection_event', { data: 'Frontend connected' })
    })
    socket.on('my_response', data => {
      data && this.setState({ response: data.data })
    });
  }

  pingWebsocket() {
    socket.emit('ping_event', { data: 'ping from frontend' });
  }

  disconnectSocket() {
    socket.emit('disconnect_request', { data: 'Frontend disconnected. Bye!' });
  }

  render() {
    const { response } = this.state;
    console.log('response', response);
    return (
      <div>
        <h3>Response from WebSocket</h3>
        {response ?
            <p>{response}</p> :
            <p>Waiting for a response...</p>}
            <button onClick={this.pingWebsocket}>Ping websocket</button>
            <button onClick={this.disconnectSocket}>Disconnect</button>
      </div>
    )
  }
}

export default WebSocket;
