const webpack = require('webpack');
const webpackDevServer = require('webpack-dev-server');
const config = require('./webpack.config');

new webpackDevServer(webpack(config), {
    publicPath: config.output.publicPath,
    hot: true,
    historyApiFallback: true,
    quiet: false,
    noInfo: false,
    stats: {
        assets: false,
        colors: true,
        version: false,
        hash: false,
        timing: false,
        chunk: false,
        chunkModules: false
    }
}).listen(3000, 'localhost', function(err) {
    if(err){
        console.log(err);
    }
    console.log('Listening at localhost:3000');
});