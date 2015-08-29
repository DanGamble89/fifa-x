import React, { Component, PropTypes } from 'react';
import $ from 'jquery';

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie != '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = $.trim(cookies[i]);
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) == (name + '=')) {
        cookieValue = decodeURIComponent(
          cookie.substring(name.length + 1)
        );
        break;
      }
    }
  }
  return cookieValue;
}

const csrfToken = getCookie('csrftoken');

function csrfSafeMethod(method) {
  // HTTP Methods that don't require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
  beforeSend: function (xhr, settings) {
    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
      xhr.setRequestHeader('X-CSRFToken', csrfToken);
    }
  }
});

class BaseComponent extends Component {
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

class CSRFToken extends BaseComponent {
  render() {
    return React.DOM.input({
      type: 'hidden',
      name: 'csrfmiddlewaretoken',
      value: csrfToken
    });
  }
}

class PlayerCategoryRow extends BaseComponent {
  render() {
    return (
      <tr>
        <th colSpan="2">{this.props.category}</th>
      </tr>
    );
  }
}

class PlayerRow extends BaseComponent {
  render() {
    return (
      <tr>
        <td>{this.props.player.fields.common_name}</td>
        <td>{this.props.player.fields.overall_rating}</td>
      </tr>
    );
  }
}

class PlayerTable extends BaseComponent {
  render() {
//    let rows = [];
//    let lastCategory = null;
//
//    this.props.products.forEach(function(product) {
//      if (product.name.indexOf(this.props.filterText) === -1 ||
// (!product.stocked && this.props.inStockOnly)) { return; }  if
// (product.category !== lastCategory) { rows.push( <PlayerCategoryRow
// category={product.category} key={product.category}/> ) }
// rows.push(<PlayerRow product={product} key={product.name}/>);  lastCategory
// = product.category; }.bind(this));

    if (this.props.players) {
      var playerRows = this.props.players.map(function (player) {
        return (
          <PlayerRow player={player} key={player.pk}/>
        )
      });
    }

    return (
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Price</th>
          </tr>
        </thead>

        <tbody>
          {playerRows}
        </tbody>
      </table>
    );
  }
}

class SearchBar extends BaseComponent {
  constructor(props) {
    super(props);

    this._bind('handleChange');
  }

  handleChange(e) {
    this.props.onUserInput(
      React.findDOMNode(this.refs.filterTextInput).value
    );
  }

  render() {
    return (
      <form>
        <CSRFToken />
        <input
          className={this.props.filterText}
          type="text"
          placeholder="Search..."
          value={this.props.filterText}
          ref="filterTextInput"
          onChange={this.handleChange} />
      </form>
    )
  }
}

class PlayerSearch extends BaseComponent {
  constructor(props) {
    super(props);

    this.state = {
      filterText: '',
      data: [],
      hasData: false
    };

    this._bind('handleUserInput', 'printState');
  }

  printState() {
    console.log(this.state);
  }

  handleUserInput(filterText) {
    if (filterText.length > 2) {
      $.ajax({
        url: '/api/players/',
        dataType: 'json',
        type: 'POST',
        data: {'text': filterText},
        success: function (data) {
          this.setState({
            data: data,
            hasData: true
          }, console.log('hey'));
          console.log('success');
        }.bind(this),
        error: function (xhr, status, err) {
          console.error('/api/players/', status, err.toString());
        }.bind(this)
      })
    } else if(filterText.length == 0) {
      this.setState({
        data: []
      })
    }

    this.setState({
      filterText: filterText
    });
  }

  render() {
    return (
      <div>
        <SearchBar
          filterText={this.state.filterText}
          onUserInput={this.handleUserInput} />

        <PlayerTable
          players={this.state.data}
          filterText={this.state.filterText} />
      </div>
    )
  }
}

export default PlayerSearch;
