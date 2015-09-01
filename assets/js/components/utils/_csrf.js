// Base imports
import React from 'react';

// Local components
import { BaseComponent } from '../_base.js';

// Utilities
import { csrfToken, csrfSafeMethod } from '../../utils/csrf';

export default class CSRFToken extends BaseComponent {
  render() {
    return React.DOM.input({
      type: 'hidden',
      name: 'csrfmiddlewaretoken',
      value: csrfToken
    });
  }
}
