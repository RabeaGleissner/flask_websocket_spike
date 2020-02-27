import React, { Component } from 'react';
import socketIOClient from 'socket.io-client';

class WebSocket extends Component {
  constructor() {
    super();
    this.state = {
      response: false,
      endpoint: 'http://127.0.0.1:5000/test',
    };
  }

  componentDidMount() {
    const { endpoint } = this.state;
    const socket = socketIOClient(endpoint);
    socket.on('connect', data => {
      console.log('socket connected, with data:', data);
      socket.emit('my_event', { data: 'Frontend connected' })
    })
    socket.on('my_response', data => this.setState({ response: data }));
  }

  render() {
    const { response } = this.state;
    return (
      <div>
        {response ?
            <p>There was this response: {response}</p> :
            <p>Waiting for a response...</p>}
      </div>
    )
  }
}

export default WebSocket;
