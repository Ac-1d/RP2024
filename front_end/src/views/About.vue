<template>
  <el-container>
    <!-- 用户信息 -->
    <el-main style="position: left; display:block;">
      <el-button type="text" @click="$store.dispatch('login', credentials)">
        改变当前用户</el-button>
      <el-button class="text-larger" style="float: left;" type="primary" icon="el-icon-caret-left"
        @click="goback()"></el-button>
      <p>用户名：{{ userInfo.username }}</p>
      <p>TOKEN-{{ userInfo.token }}</p>
    </el-main>

    <el-main style="position: left; display:block;">
      <el-input v-model="credit.username"></el-input>
      <el-input v-model="credit.password"></el-input>
      <el-button @click="Login">login</el-button>
      <el-button type="primary" @click="GetNovels">获取全部小说资源</el-button>
    </el-main>

    <el-main>
      
    </el-main>
  </el-container>
</template>

<script>
import { login } from '@/js/Api.js';
import { novels } from '@/js/Api.js';
export default {
  data() {
    return {
      credit: { username: '', password: '' },
      userInfo: this.$store.state,
      credentials: {
        isLoggedIn: true,
        token: '23456789',
      },
    }
  },
  methods: {
    Login() {
      let returnVal = login(this.credit.username, this.credit.password);
      console.log(returnVal);
    },
    GetNovels() {
      let returnVal = novels();
      console.log(returnVal);
    }
  }
}
</script>
