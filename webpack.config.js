const path = require('path')
const webpack = require('webpack')
const ExtractTextPlugin = require("extract-text-webpack-plugin");
const NODE_ENV = process.env.NODE_ENV || 'development';
const CompressionPlugin = require("compression-webpack-plugin");

module.exports = {
  entry:  ['babel-polyfill', './frontend/static/js/application.js'],
  output: {
    path: __dirname + '/frontend/static/dist',
    publicPath: '/static/dist/',
    filename: '[name].js?[hash]',
    library: '[name]'
  },
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader',
        options: {
          loaders: {
          }
          // other vue-loader options go here
        }
      },
      {
        test: /\.css$/,
        use: [ 'style-loader', 'css-loader' ]
      },
      {
        test: /\.js$/,
        loader: 'babel-loader',
        exclude: /node_modules/
      },
      {
        test: /\.svg$/,
        loader: 'vue-svg-loader', // `vue-svg` for webpack 1.x
      },
      {
        test: /\.(png|jpg|gif)$/,
        loader: 'file-loader',
        options: {
          name: '[name].[ext]?[hash]'
        }
      },
      {
        test: /\.styl$/,
        use:  ['css-hot-loader'].concat(ExtractTextPlugin.extract({
          use: [
            { loader: 'css-loader', options: { sourceMap: true}},
            { loader: 'postcss-loader', options: { sourceMap: true}},
            { loader: 'stylus-loader', options: { sourceMap: true}}
          ]
        }))
      },
      {
        test: /\.(eot|ttf|woff|woff2)$/,
        loader: 'file-loader',
        query: {
          name: '[name].[ext]?[hash]'
        }
      },
      {
        test: /\.modernizrrc$/,
        loader: "modernizr-loader!json-loader"
      },
    ]
  },
  node: {
    fs: 'empty'
  },
  resolve: {
    alias: {
      'vue$': 'vue/dist/vue.esm.js',
      modernizr$: path.resolve(__dirname, ".modernizrrc")
    }
  },
  watch: NODE_ENV === 'development',
  plugins: [
    new webpack.optimize.CommonsChunkPlugin({
      name: "vendor",
      minChunks: function (module) {
        return module.context && module.context.indexOf("node_modules") !== -1;
      }
    }),
    new webpack.optimize.OccurrenceOrderPlugin(),
    new webpack.NoEmitOnErrorsPlugin(),
    new ExtractTextPlugin("css/[name].css?[hash]"),
    new CompressionPlugin({
      asset: "[path].gz[query]",
      algorithm: "gzip",
      test: /\.js$|\.css$|\.html$/,
      threshold: 10240,
      minRatio: 0.8
    }),
  ],
  devServer: {
    historyApiFallback: true,
    contentBase: __dirname + '/frontend/templates',
    host: 'localhost',
    port: 3000,
    inline: true,
    hot: true,
    proxy: [{
      path: '**',
      target: 'http://127.0.0.1:8000/'
    }]
  },
  performance: {
    hints: false
  },
  devtool: NODE_ENV === 'development' ? "source-map" : '#cheap-module-eval-source-map',
};

if (process.env.NODE_ENV === 'production') {
  module.exports.devtool = '#source-map'
  module.exports.plugins = (module.exports.plugins || []).concat([
    new webpack.DefinePlugin({
      'process.env': {
        NODE_ENV: '"production"'
      }
    }),
    new webpack.optimize.UglifyJsPlugin({
      beautify: false,
      comments: false,
      compress: {
        sequences: true,
        booleans: true,
        loops: true,
        unused: true,
        warnings: false,
        drop_console: true,
        unsafe: true
      }
    }),
    new webpack.LoaderOptionsPlugin({
      minimize: true
    }),
  ])
}
