// Base imports
import React, { Component, PropTypes } from 'react';
import $ from 'jquery';

// Local components
import { BaseComponent } from '../_base.js';
import CSRFToken from '../utils/_csrf.js';

class Player extends BaseComponent {
  render() {
    const player = this.props.player;
    const playerUrl = `/players/${player.slug}`;
    const playerClass = `playerList_item ${player.css_class}`;

    return (
      <li className="list_item">
        <a className={playerClass} href={playerUrl}>
          <img
            className="playerList_img playerList_img-player"
            alt={player.common_name}
            src={player.image_medium}
            height="36"/>
          <img
            className="playerList_img playerList_img-club"
            alt={player.common_name}
            src={player.club__image_medium}
            height="24" />
          <img
            className="playerList_img playerList_img-nation"
            alt={player.common_name}
            src={player.nation__image_medium}
            width="30" />
          <span className="playerList_name">{player.common_name}</span>
          <span className="playerList_rating">{player.overall_rating}</span>
          </a>
      </li>
    );
  }
}

class PlayerList extends BaseComponent {
  render() {
    if (this.props.players.length > 0 && this.props.hasData) {
      // If a legit search has been made and a player has been returned
      var playerNodes = this.props.players.map(function (player) {
        return (
          <Player player={player} key={player.pk}/>
        )
      });
    } else if (this.props.hasData) {
      // If a legit search has been made but the input form has been cleared
      var playerNodes = (<li>There are no players</li>)
    }

    return (
      <ul className="playerList [ list ]">
        {playerNodes}
      </ul>
    )
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

        <PlayerList
          players={this.state.data}
          filterText={this.state.filterText}
          hasData={this.state.hasData}/>
      </div>
    )
  }
}

export default React.render(<PlayerSearch />, document.getElementById('PlayerSearch'));
