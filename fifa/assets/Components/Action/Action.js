import template from './Action.html';
import './Action.scss';

export default {
  props: ['link'],

  template: template,

  methods: {
    handleClick(e) {
      e.preventDefault();

      console.log(this.link);
    }
  }
}
