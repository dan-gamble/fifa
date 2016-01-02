var path = require('path')
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')
var ExtractTextPlugin = require('extract-text-webpack-plugin')

module.exports = {
  context: __dirname,

  entry: [
    'webpack-dev-server/client?http://localhost:3000',
    'webpack/hot/only-dev-server',
    './fifa/assets/js/index'
  ],

  output: {
    path: path.resolve('./fifa/static/bundles'),
    filename: '[name].js',
    publicPath: 'http://localhost:3000/static/bundles/'
  },

  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoErrorsPlugin(),
    new BundleTracker({filename: './webpack-stats.json'}),
    new ExtractTextPlugin('[name].css')
  ],

  module: {
    loaders: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
        query: {
          presets: ['es2015', 'stage-0'],
          plugins: ['transform-runtime']
        }
      },
      {
        test: /\.vue$/,
        loader: 'vue'
      }
    ]
  },

//  vue: {
//    loaders: {
//      css: ExtractTextPlugin.extract('css')
//    }
//  },

  resolve: {
    modulesDirectories: ['node_modules'],
    extensions: ['', '.js']
  },

  vue: {
    autoprefixer: {
      browsers: ['last 2 versions']
    }
  }
}
