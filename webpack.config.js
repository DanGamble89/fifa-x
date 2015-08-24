var path = require('path');
var ExtractTextPlugin = require("extract-text-webpack-plugin");
var BundleTracker = require('webpack-bundle-tracker');
var BrowserSyncPlugin = require('browser-sync-webpack-plugin');

module.exports = {
  devtool: 'source-map',
  entry: path.resolve(__dirname, 'fifa/assets/main.js'),
  output: {
    path: path.resolve(__dirname, 'fifa/static/bundles'),
    filename: 'bundle.js'
  },
  module: {
    loaders: [
      {
        test: path.join(__dirname, 'fifa/assets'),
        loader: 'babel-loader'
      },
      {
        test: /\.scss$/,
        loader: ExtractTextPlugin.extract(
          // activate source maps via loader query
          'css?sourceMap!autoprefixer?browsers=last 2 version!' +
          'sass?sourceMap'
        )
      },
      {
        test: /\.(png|jpg)$/,
        loader: 'url-loader?limit=25000'
      }
    ]
  },
  plugins: [
    new BundleTracker({filename: './webpack-stats.json'}),
    new ExtractTextPlugin("styles.css"),
    new BrowserSyncPlugin({
      injectChanges: true,
      logFileChanges: true,
      logPrefix: 'text',
      notify: false,
      open: false,
      proxy: '0.0.0.0:8000'
    })
  ],
  resolve: {
    modulesDirectories: ['node_modules', 'bower_components'],
    extensions: ['', '.js', '.jsx']
  },
};
