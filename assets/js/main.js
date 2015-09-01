// Base imports
import React, { Component, PropTypes } from 'react';
import $ from 'jquery';

// Local components
import { BaseComponent } from './components/_base.js';
import CSRFToken from './components/utils/_csrf.js';

import './components/TopBar/_PlayerSearch.js';

// Utilities
import { csrfToken, csrfSafeMethod } from './utils/csrf';

/**
 * Set the CSRF token for AJAX posting
 */
$.ajaxSetup({
  beforeSend: function (xhr, settings) {
    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
      xhr.setRequestHeader('X-CSRFToken', csrfToken);
    }
  }
});
