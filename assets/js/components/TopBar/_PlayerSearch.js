// Base imports
import React, { Component, PropTypes } from 'react';
import $ from 'jquery';

// Local components
import { BaseComponent } from '../_base.js';
import CSRFToken from '../utils/_csrf.js';

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
    const playerUrl = `/players/${player.fields.slug}`;

    return (
      <tr>
        <td><a href={playerUrl}>{player.fields.common_name}</a></td>
        <td>{player.fields.overall_rating}</td>
      </tr>
    );
  }
}

class PlayerTable extends BaseComponent {
  render() {
    if (this.props.players.length > 0 && this.props.hasData) {
      var playerRows = this.props.players.map(function (player) {
        return (
          <PlayerRow player={player} key={player.pk}/>
        )
      });
    } else if (this.props.hasData) {
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
          onChange={this.handleChange}/>
      </form>
    )
  }
}

export default class PlayerSearch extends BaseComponent {
  constructor(props) {
    super(props);

    this.state = {
      filterText: '',
      data: [],
      hasData: false
    };

    this._bind('handleUserInput');
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
    } else if (filterText.length == 0) {
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
          onUserInput={this.handleUserInput}/>

        <PlayerTable
          players={this.state.data}
          filterText={this.state.filterText}
          hasData={this.state.hasData}/>
      </div>
    )
  }
}

export default React.render(<PlayerSearch />, document.getElementById('react-app'));
