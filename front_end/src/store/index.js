import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    isLoggedIn: false, // 初始登录状态为false 
    username: 'lzy',
    token: '12345678',
  },
  mutations: {
    LOGIN(state, payload) {  
      // 假设payload是一个对象，包含了登录后的数据，如用户名、token等  
      state.isLoggedIn = true;
      // 你可以在这里设置其他登录后的状态  
      state.username = payload.username; 
      state.token = payload.token;
    },  
    LOGOUT(state) {  
      state.isLoggedIn = false  ;
      // 你可以在这里清除其他登录相关的状态  
      // state.username = null  
      // state.token = null  
    }  
  },
  actions: {
    login({ commit }, payload) {  
      // 这里通常是一个异步操作，比如发送一个API请求来验证登录凭据  
      // 假设验证成功，我们提交一个mutation来改变状态  
      commit('LOGIN', payload);
    },  
    logout({ commit }) {  
      // 同样，这里可能包含一些清理逻辑，比如删除token等  
      this.state.token = '';
      // 然后我们提交一个mutation来改变状态  
      commit('LOGOUT');
    }  
  },
  getters: {
    isLoggedIn: state => state.isLoggedIn,  
    
  },
  modules: {}
});
