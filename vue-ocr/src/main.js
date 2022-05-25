import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import store from './store'
import './plugins/element.js' 
import './assets/css/reset.css'
import './assets/css/iconfont.css'


Vue.config.productionTip = false
//全局挂载axios
Vue.prototype.$axios = axios

new Vue({
  router,
  axios,
  store,
  render: h => h(App),
}).$mount('#app')
