module.exports = {
    devServer: {
        proxy: {
            "^/": {
                target: "http://localhost:8090"
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
