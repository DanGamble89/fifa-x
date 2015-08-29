import React, { Component, PropTypes } from 'react';

class BaseComponent extends Component {
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
    const name = this.props.product.stocked ?
      this.props.product.name :
      <span style={{color: 'red'}}>
        {this.props.product.name}
      </span>;

    return (
      <tr>
        <td>{name}</td>
        <td>{this.props.product.price}</td>
      </tr>
    );
  }
}

class PlayerTable extends BaseComponent {
  render() {
    console.log(this.props);

    let rows = [];
    let lastCategory = null;

    this.props.products.forEach(function(product) {
      if (product.name.indexOf(this.props.filterText) === -1 || (!product.stocked && this.props.inStockOnly)) {
        return;
      }

      if (product.category !== lastCategory) {
        rows.push(
          <PlayerCategoryRow category={product.category} key={product.category}/>
        )
      }

      rows.push(<PlayerRow product={product} key={product.name}/>);

      lastCategory = product.category;
    }.bind(this));

    return (
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Price</th>
          </tr>
        </thead>

        <tbody>
          {rows}
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
    console.log(this.refs);

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
      inStockOnly: false
    };

    this._bind('handleUserInput');
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
          products={this.props.products}
          filterText={this.state.filterText}
          inStockOnly={this.state.inStockOnly} />
      </div>
    )
  }
}

export default PlayerSearch;
