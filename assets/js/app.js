import React, { Component, PropTypes } from 'react';
import $ from 'jquery';

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

  handleChange() {
    /**
     *
     */
    this.props.onUserInput(
      React.findDOMNode(this.refs.filterTextInput).value,
      React.findDOMNode(this.refs.inStockOnlyInput).checked
    );
  }

  render() {
    return (
      <form>
        <input
          type="text"
          placeholder="Search..."
          value={this.props.filterText}
          ref="filterTextInput"
          onChange={this.handleChange} />

        <p>
          <input
            type="checkbox"
            checked={this.props.inStockOnly}
            ref="inStockOnlyInput"
            onChange={this.handleChange} />
          {' '}
          Only show products in stock
        </p>
      </form>
    )
  }
}

class PlayerSearch extends BaseComponent {
  constructor(props) {
    super(props);

    this.state = {
      filterText: '',
      inStockOnly: false,
      data: []
    };

    this._bind('handleUserInput', 'loadPlayers');
  }

  loadPlayers() {
    $.ajax({
      url: '/api/players',
      dataType: 'json',
      cache: false,
      success: function (data) {
        this.setState({data: JSON.parse(data)});
      }.bind(this),
      error: function (xhr, status, err) {
        console.error('/api/players/', status, err.toString());
      }.bind(this)
    });
  }

  componentDidMount() {
    this.loadPlayers();

    setInterval(this.loadPlayers, 2000);
  }

  handleUserInput(filterText, inStockOnly) {
    this.setState({
      filterText: filterText,
      inStockOnly: inStockOnly
    });
  }

  render() {
    return (
      <div>
        <SearchBar
          filterText={this.state.filterText}
          inStockOnly={this.state.inStockOnly}
          onUserInput={this.handleUserInput} />

        <PlayerTable
          players={this.state.data}
          filterText={this.state.filterText}
          inStockOnly={this.state.inStockOnly} />
      </div>
    )
  }
}

export default PlayerSearch;
