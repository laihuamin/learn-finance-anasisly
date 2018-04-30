const webpack = require('webpack');
const path = require('path');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const extractPlugin = new ExtractTextPlugin({
    filename: 'main.css'
});
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CleanWebpackPlugin = require('clean-webpack-plugin');

module.exports = {
    entry: './src/index.js',
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: '[name].js',
        publicPath: '/'
    },
    resolve: {
        extensions: ['.js', '.jsx'],  //这样就可以在引用的时候不加扩展名
        alias: {
            components: path.resolve(__dirname, './src/components'),
            commons: path.resolve(__dirname, './src/commons')
        }
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                use: [
                    {
                        loader: 'babel-loader',
                        options: {
                            presets: ['es2015', 'react']
                        }
                    }
                ]
            },
            {
                test: /\.less$/,
                use: extractPlugin.extract({
                    use: ['css-loader', 'less-loader']
                })
            },
            {
                test: /\.html$/,
                use: ['html-loader']
            },
            {
                test: /\.(png|jpg|gif)/,
                use: [
                    {
                        loader: 'url-loader',
                        options: {
                            limit: 2048
                        }
                    }
                ]
            }
        ]
    },
    plugins: [
        new HtmlWebpackPlugin({
            template: 'index.tpl.html',
            inject: 'body',
            filename: 'index.html'
        }),
        new CleanWebpackPlugin(['dist']),
        new webpack.optimize.OccurrenceOrderPlugin(),
        new webpack.HotModuleReplacementPlugin(),
        new webpack.NoEmitOnErrorsPlugin(),
        new webpack.DefinePlugin({
            'process.env.NODE_ENV': JSON.stringify('development')
        }),
        new webpack.optimize.CommonsChunkPlugin({
            names: ['commons'], // 这公共代码的chunk名为'commons'
            filename: 'dist/js/[name].bundle.js', // 生成后的文件名，虽说用了[name]，但实际上就是'commons.bundle.js'了
            minChunks: 4
        }),
        extractPlugin
    ]
}