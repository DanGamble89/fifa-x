import { Component } from 'react';

export class BaseComponent extends Component {
  /**
   * When using React with ES6 we lose the magical this binding of
   * React.createClass() This creates a method that binds this on all the
   * functions our class creates
   * @param methods
   * @private
   *
   * @example
   * this._bind('function1', 'function2')
   */
  _bind(...methods) {
    methods.forEach((method) => this[method] = this[method].bind(this));
  }
}
