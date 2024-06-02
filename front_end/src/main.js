import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import axios from 'axios';

Vue.use(ElementUI);

Vue.prototype.$axios = axios;

axios.defaults.baseURL = 'http://127.0.0.1:8000'; // 设置请求的基地址 

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount("#app");

// import axios from 'axios';  
 
axios.get('users/login')  
  .then(response => {  
    // 处理响应数据  
    console.log(response.data);  
  })  
  .catch(error => {  
    // 处理错误  
    console.error(error);  
  });
