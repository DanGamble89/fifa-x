var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
var ExtractTextPlugin = require('extract-text-webpack-plugin');

var cssLoaders = ['style', 'css', 'autoprefixer-loader?browsers=last 2 versions'];

module.exports = {
  watch: true,

  context: __dirname,

  entry: [
    './assets/js/index'
  ],

  devtool: 'source-map',

  output: {
    path: path.resolve('./fifa/static/js'),
    filename: 'main.js',
    publicPath: '/static/js/'
  },

  module: {
    loaders: [
      // Transform JSX
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        loaders: ['react-hot', 'babel?stage=0']
      },
      {
        test: /\.scss$/,
        loaders: cssLoaders.concat([
          'sass'
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
//    new webpack.HotModuleReplacementPlugin(),
//    new webpack.NoErrorsPlugin(),
    new BundleTracker({filename: './webpack-stats.json'}),
//    new ExtractTextPlugin('styles.css')
  ],

  resolve: {
    modulesDirectories: ['node_modules', 'bower_components'],
    extensions: ['', '.js', '.jsx']
  }
};
