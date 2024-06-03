<template>
  <el-container>
    <!-- 用户信息 -->
    <el-main style="position: left; display:block;" v-if="$store.state.loggedIn">
      <p>用户名：{{ $store.state.userinfo.username }}</p>
      <p>TOKEN-{{ $store.state.userinfo.token }}</p>
    </el-main>

    <el-main style="position: left; display:block;">
      <el-input v-model="credit.username"></el-input>
      <el-input v-model="credit.password"></el-input>

      <el-button @click="userlogin">login</el-button>
      <el-button @click="$store.dispatch('logout')">logout</el-button>

      <!-- <el-button type="primary" @click="GetNovels">获取全部小说资源</el-button> -->
    </el-main>

    <el-main>
      
    </el-main>
  </el-container>
</template>

<script>

export default {
  data() {
    return {
      credit: { username: '', password: '' },
    }
  },
  methods: {
    userlogin() {
      this.$store.dispatch('login', this.credit);
    }
  }
}
</script>
