import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify';
import axios from 'axios'

Vue.config.productionTip = false
Vue.prototype.$axios = axios;
Vue.prototype.$axios.defaults.headers.common['x-cds-authentication'] = 'yjWq0Nv5bJOE3sZBZ4sGuK1KNHkD9KTX'
// Vue.prototype.$axios.defaults.baseURL = 'http://127.0.0.1:8080';

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
