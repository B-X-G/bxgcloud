var webpack = require('webpack');
var ExtractTextPlugin = require("extract-text-webpack-plugin");

// 传入参数website以满足同时处理多个website的条件
var websites = ['mobile'];
var website = process.env.NODE_ENV;
if (website.indexOf(websites) === -1) {
    console.log("not support this website");
    return;
}

var website2files = {
    'mobile': {
        'entry': {
            'js': './static/mobile/js/react/app.js',
            'scss': './static/mobile/scss/index.scss'
        },
        'dist': {
            'js': './static/mobile/dist/mobile.app.min.js',
            'css': './static/mobile/dist/mobile.app.min.css'
        }
    }
};

module.exports = {
        entry: website2files[website].entry.js,
        output: {
            path: __dirname,
            filename: website2files[website].dist.js
        },
        module: {
            loaders: [
                {
                    test: /\.(js|jsx)$/,
                    loader: 'babel-loader',
                    exclude: /node_modules/,
                    query: {
                        presets: ['es2015', 'stage-0', 'react']
                    }
                },
                {
                    test: /\.scss$/,
                    loader: ExtractTextPlugin.extract('css!sass')
                }
            ]
        },
        plugins: [
            new webpack.optimize.UglifyJsPlugin({
                compress: {
                    warnings: true
                },
                output: {
                    comments: true
                }
            }),
            new ExtractTextPlugin(website2files[website].dist.css, {
                allChunks: true
            })
        ],
        resolve: {
            extensions: ['', '.js', '.jsx']
        }
    };