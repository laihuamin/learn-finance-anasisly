const dev = require('./dev.js');
const prod = require('./prod.js');

module.exports = {
    dev: {
        env: dev,
        assetsRoot: path.resolve(__dirname, '../dist'),
		assetsSubDirectory: 'static',
	    cssSourceMap: true
    },
    prod: {
        env: prod,
        assetsRoot: path.resolve(__dirname, '../dist'),
		assetsSubDirectory: 'static',
	    cssSourceMap: false
    }
}