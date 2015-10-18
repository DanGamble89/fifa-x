import Vue from 'vue';

import Action from './Components/Action/Action.js';

import './index.scss';

const app = {
  components: {
    'action': Action
  }
};

new Vue(app).$mount('body');
