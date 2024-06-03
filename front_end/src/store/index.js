import Vue from "vue";
import Vuex from "vuex";
import axios from 'axios';  

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    loggedIn: false, // 状态：是否已经登录
    userinfo: null, // 用户信息，登录后设置
  },
  mutations: {
    LOGIN(state, data) { 
      // data是登录请求返回数据
      state.loggedIn = true;
      state.userinfo = data;
    },  
    LOGOUT(state) {  
      state.loggedIn = false;
      state.userinfo = null;
    },
    setShowTopBar(state) {
      console.log("call set show top bar")
      state.showNavBar = !state.showNavBar
    }
  },
  actions: {
    async login({ commit }, loginData) {  
      let username = loginData.username;
      let password = loginData.password;
      if (username && password) {
        await axios.post("/users/login", {  
          username: username,  
          password: password,
        }).then(response => {
          if (response.data.status == 200 && response.data.msg == '登录成功') {
            commit('LOGIN', response.data);
            return '登录成功';
          }
        }).catch(error => {
          // console.log(error.response);
          if (error.response.status == 400) return '用户名或密码错误';
          else return '其他错误';
        })
      }
    },  
    logout({ commit }) {
      commit('LOGOUT');
    },

  },
  getters: {
    loggedIn: state => state.loggedIn,  
    
  },
  modules: {}
});
