import React, { Component, PropTypes } from 'react';

class MyComponent extends React.Component {
  constructor(props) {
    super(props);
    this._handleClick = this._handleClick.bind(this);
  }

  static defaultProps = {
    autoPlay: false,
    maxLoops: 10
  }

  _handleClick() {
    console.log(this);
  }

  render() {
    return (
      <input type="text" placeholder="finally?" onClick={this._handleClick} />
    )
  }
}

export default MyComponent;
