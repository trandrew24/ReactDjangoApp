// webpack bundles our javascript into one file for the browser (transpile?)
const path = require("path");
const webpack = require("webpack");

module.exports = {
  entry: "./src/index.js", // relative path
  output: {
    path: path.resolve(__dirname, "./static/frontend"), // gets the current directory we're in and shoves it in the ./static/frontend folder
    filename: "[name].js",
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
        },
      },
    ],
  },
  optimization: {
    minimize: true,  // makes our javascript smaller (gets rid of white space)
  },
  plugins: [
    new webpack.DefinePlugin({
      "process.env": {
        // This has effect on the react lib size
        // NODE_ENV: JSON.stringify("production"),
        // CHANGED TO THIS, SUGGESTED FROM REDDIT AND STACKOVERFLOW
        NODE_ENV: JSON.stringify("development"),
      },
    }),
  ],
};