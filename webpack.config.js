var path = require('path');

var webpack    = require('webpack');
var production = process.env.NODE_ENV === 'production';
var CleanPlugin = require('clean-webpack-plugin');
var ExtractPlugin = require('extract-text-webpack-plugin');

var plugins = [
  // This plugins optimizes chunks and modules by
  // how much they are used in your app
  new webpack.optimize.OccurenceOrderPlugin(),
  new ExtractPlugin(production ? '[name]-[hash].css' : 'bundle.css'),
  new webpack.HotModuleReplacementPlugin(),
  new webpack.NoErrorsPlugin()
];

if (production) {
  plugins = plugins.concat([
    // This plugin looks for similar chunks and files
    // and merges them for better caching by the user
    new webpack.optimize.DedupePlugin(),
    // This plugin prevents Webpack from creating chunks
    // that would be too small to be worth loading separately
    new webpack.optimize.MinChunkSizePlugin({
      minChunkSize: 51200, // ~50kb
    }),
    // This plugin minifies all the Javascript code of the final bundle
    new webpack.optimize.UglifyJsPlugin({
      mangle: true,
      compress: {
        warnings: false, // Suppress uglification warnings
      }
    }),
    // Cleanup the builds/ folder before
    // compiling our final assets
    new CleanPlugin('fifa/static'),
    // This plugins defines various variables that we can set to false
    // in production to avoid code related to them from being compiled
    // in our final bundle
    new webpack.DefinePlugin({
      __SERVER__: !production,
      __DEVELOPMENT__: !production,
      __DEVTOOLS__: !production,
      'process.env': {
        BABEL_ENV: JSON.stringify(process.env.NODE_ENV)
      }
    })
  ]);
}

module.exports = {
  debug: !production,

  devtool : production ? false : 'eval',

  context: path.join(__dirname, 'fifa', 'assets'),

  entry: [
    'webpack/hot/dev-server',
    'webpack-hot-middleware/client',
    './index'
  ],

  output: {
    path: path.join(__dirname, 'fifa', 'static'),
    filename: production ? '[name]-[hash].js' : 'bundle.js',
    chunkFilename: '[name]-[chunkhash].js',
    publicPath: '/static/'
  },

  module: {
    loaders: [
      {
        test: /\.js/,
        exclude: /node_modules/,
        loader: 'babel',
        include: __dirname + '/fifa/assets'
      },
      {
        test: /\.scss/,
        loader: ExtractPlugin.extract('style', 'css!sass')
      },
      {
        test: /\.html/,
        loader: 'html'
      },
      {
        test: /\.(png|gif|jpe?g|svg)$/i,
        loader: 'url',
        query: {
          limit: 10000
        }
      }
    ]
  },

  plugins: plugins,


  resolve: {
    modulesDirectors: ['node_modules']
  }
};
