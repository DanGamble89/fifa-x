import React, { Component, PropTypes } from 'react';
import $ from 'jquery';

import {csrfToken, csrfSafeMethod} from './utils/csrf';

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
    const player = this.props.player;
    const playerUrl = `/players/${this.props.player.fields.slug}`;

    return (
      <tr>
        <td><a href={playerUrl}>{player.fields.common_name}</a></td>
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

    console.log(this.props);

    if (this.props.players.length > 0 && this.props.hasData) {
      var playerRows = this.props.players.map(function (player) {
        return (
          <PlayerRow player={player} key={player.pk}/>
        )
      });
    } else if(this.props.hasData) {
      var playerRows = (<td colspane="2">There are no players</td>)
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
          });
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
          filterText={this.state.filterText}
          hasData={this.state.hasData} />
      </div>
    )
  }
}

export default PlayerSearch;
