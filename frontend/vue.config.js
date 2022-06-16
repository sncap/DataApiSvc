module.exports = {
    devServer: {
        proxy: {
            "^/": {
                target: "http://34.168.167.28:8090"
            }
        },
        disableHostCheck: true
    },
  "transpileDependencies": [
    "vuetify"
  ],
  chainWebpack: config => {
    config.module.rules.delete('eslint');
  }
}
