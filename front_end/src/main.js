import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import axios from 'axios';

Vue.use(ElementUI);

Vue.prototype.$axios = axios;

axios.defaults.baseURL = 'http://47.93.0.24:8000'; // 设置请求的基地址 改为网站的ip地址

Vue.config.productionTip = false;
Vue.use(ElementUI);

new Vue({
  router,  
  store,
  render: h => h(App),
}).$mount("#app");