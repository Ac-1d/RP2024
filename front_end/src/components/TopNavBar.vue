<template>
  <div class="top-nav-bar" v-if="showNavBar">
    <div class="left-links">
      <router-link to="/">主页</router-link>
      <router-link to="/BookShelf">书架</router-link>
      <router-link to="/creation">创作中心</router-link>
      <router-link to="/mail">站内信</router-link>
      <router-link to="/Center">个人中心</router-link>

    </div>
    <div class="right-links">
    <template v-if="!isLoggedIn">
      <el-button class='button' type="text" @click="show_logBox">登录</el-button>
      <Login_window :dialogflag="showLog" @closedia="closeLog"  ></Login_window>
    </template>

    <template v-if="isLoggedIn">
      <el-button class='button' type="text" @click="logout">登出</el-button>
    </template>

      <el-button class='button' type="text" @click="show_regBox">注册</el-button>
      <Register_window :dialogflag="showRegis" @closedia="closeRegis"  ></Register_window>

    </div>
  </div>
</template>

<script>
import Login_window from "@/components/Login_window.vue"
import Register_window from "@/components/Register_window.vue"
import { mapState } from 'vuex';
export default {
  name: "TopNavBar",
  components: { Login_window , Register_window},
  data() {
    return {
      // showNavBar: true,
      showLog: true, // Boolean 用于dialog隐藏/显示
      showRegis:false,
    }
  },
  methods: {
    show_logBox() {
      this.showLog = true;
      // 可以在此处添加更多登录逻辑
    },
    show_regBox() {
      this.showRegis = true;
      // 可以在此处添加更多登录逻辑
    },

    closeLog() {
      this.showLog = false;
    },
    closeRegis() {
      this.showRegis = false;
      console.log(this.showRegis);
    },
    logout(){
      this.$store.dispatch('logout');
      alert('已登出');
    },

  },
  computed: {
    ...mapState(['showNavBar']),
    isLoggedIn() {
        return this.$store.getters.loggedIn;
    },
  },
};
</script>

<style scoped>
.top-nav-bar {
  display: flex;
  justify-content: space-between;
  padding: 10px 20px;
  background-color: #4e4e4e;
  color: white;
}
.left-links a, .right-links a {
  margin-right: 15px;
  color: white;
  text-decoration: none;
}
.left-links a:hover, .right-links a:hover {
  text-decoration: underline;
}
.right-links {
  margin-left: auto;
}
.button{
    margin-left:5px;
}
</style>
