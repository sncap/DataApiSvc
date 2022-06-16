module.exports = {
    devServer: {
        proxy: {
            "^/": {
                target: "http://${DEST_URL}:8090"
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
