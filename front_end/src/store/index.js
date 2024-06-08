import Vue from "vue";
import Vuex from "vuex";
import axios from 'axios';  

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    loggedIn: false, // 状态：是否已经登录
    verify: null, // 用户登录时的身份验证结果
    userInfo: null,
    showNavBar: true,
    currentBookId: null,
    currentChapterId: null,
  },
  mutations: {
    LOGIN(state, data) { 
      // data是登录请求返回数据
      state.loggedIn = true;
      state.verify = data;
    },  
    LOGOUT(state) {  
      state.loggedIn = false;
      state.verify = null;
      state.userInfo = null;
    },
    setShowTopBar(state) {
      console.log("call set show top bar")
      state.showNavBar = !state.showNavBar
    },
    GetUserInfo(state, userInfo) {//为什么一个get方法是修改userInfo的值？
      state.userInfo = userInfo;
    },
    setCurrentBookId(state, bookId){
      state.currentBookId = bookId
    },
    setCurrentChapterId(state, chapterId){
      console.log("set current chapter id to ", chapterId)
      state.currentChapterId = chapterId
    }
  },
  actions: {
    async login({ commit }, loginData) { 
      let mobile = loginData.mobile;
      let password = loginData.password;
      let msg = '登录失败';
      if (mobile && password) {
        await axios.post("/users/login", {  
          mobile: mobile,
          password: password,
        }).then(response => {
          if (response.data.status == 200 && response.data.msg == '登录成功') {
            commit('LOGIN', response.data);
            msg = '登录成功';
          }
        }).catch(error => {
          msg = '验证失败，错误码：' + error.response.status;
          alert("登录失败，用户不存在或密码错误");
        })
      }
      return {msg: msg};
    },  
    logout({ commit }) {
      commit('LOGOUT');
    },
    async getUserInfo({ commit }) {  
      if (!this.state.loggedIn) return '请先登录';
      let token = this.state.verify.token;  
      await axios.get('/users/userinfo', {  
        headers: {  
          'Authorization': `Bearer ${token}`  
        }  
      }).then (response => {
        commit('GetUserInfo', response.data.info);
        return response.data.info;
      }).catch (error => {  
        console.error(error);
        return '出现错误';
      })
    }
  },
  getters: {
    loggedIn: state => state.loggedIn,  
    showNavBar: state => state.showNavBar,
    userInfo: state => state.userInfo,
  },
  modules: {}
});
