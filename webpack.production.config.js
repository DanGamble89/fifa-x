var BundleTracker = require('webpack-bundle-tracker');

config = require('./webpack.config.js');

config.output.path = require('path').resolve('./fifa/static/dist');

config.plugins = [
  new BundleTracker({filename: './webpack-stats-prod.json'})
];

// override any other settings here like using Uglify or other things that make
// sense for production environments.

module.exports = config;
