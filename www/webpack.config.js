const path = require("path");

module.exports = {
  entry: "./scripts/main.js",
  output: {
    path: path.join(__dirname, "build"),
    filename: "main.js"
  },
  devServer: {
    contentBase: path.join(__dirname),
    compress: true,
    open: true,
    port: 8080,
    historyApiFallback: {
      index: "new.html"
    }
  },
  module: {
    rules: [
      // {
      //   test: /\.js$/,
      //   exclude: /(node_modules)/,
      //   use: {
      //     loader: "babel-loader",
      //     options: {
      //       presets: ["env"]
      //     }
      //   }
      // },
      // {
      //   test: /\.scss$/,
      //   use: [
      //     { loader: "style-loader" },
      //     { loader: "css-loader" },
      //     { loader: "sass-loader" }
      //   ]
      // },
      // {
      //   test: /\.(jpg|svg|png|ttf)$/,
      //   loader: "url-loader"
      // }
    ]
  }
  //   plugins: [new UglifyJsPlugin()]
};
