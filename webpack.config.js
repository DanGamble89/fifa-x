var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
var ExtractTextPlugin = require('extract-text-webpack-plugin');

cssLoaders = ['style', 'css?sourceMap', 'csslint', 'autoprefixer-loader?browsers=last 2 versions'];

module.exports = {
  context: __dirname,

  entry: [
    'webpack-dev-server/client?http://localhost:3000',
    'webpack/hot/only-dev-server',
    './assets/js/index'
  ],

  devtool: 'source-map',

  output: {
    path: path.resolve('./fifa/static/bundles'),
    filename: '[name]-[hash].js',
    publicPath: 'http://localhost:3000/static/bundles/'
  },

  module: {
    loaders: [
      // Transform JSX
      {
        test: /\.jsx$/,
        exclude: /node_modules/,
        loaders: ['react-hot', 'babel-loader']
      },
      {
        test: /\.scss$/,
        loaders: cssLoaders.concat([
          'sass?sourceMap?precision=10'
        ])
      },
//      {
//        test: /\.scss$/,
//        loader: ExtractTextPlugin.extract(
//          'css?sourceMap!' + 'sass?sourceMap'
//        )
//      },
      {
        test: /\.(png|jpg)$/,
        loader: 'url?limit=25000'
      }
    ]
  },

  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoErrorsPlugin(),
    new BundleTracker({filename: './webpack-stats.json'}),
//    new ExtractTextPlugin('styles.css')
  ],

  resolve: {
    modulesDirectories: ['node_modules', 'bower_components'],
    extensions: ['', '.js', '.jsx']
  }
};
