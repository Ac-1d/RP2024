<template>
  <el-container>
    <!-- 用户信息 -->
    <el-main style="position: left; display:block;" v-if="$store.state.userInfo">
      <!-- 如果userInfo为空，就不加载，从而避免了报错 -->
      <p>用户名：{{ $store.state.userInfo.username }}</p>
      <p>ID-{{ $store.state.userInfo.id }}</p>
    </el-main>

    <el-main style="position: left; display:block;">
      <el-input v-model="credit.username"></el-input>
      <el-input v-model="credit.password"></el-input>

      <el-button @click="userlogin">login</el-button>
      <el-button @click="$store.dispatch('logout')">logout</el-button>
      <el-button @click="$store.dispatch('getUserInfo')">'getUserInfo'</el-button>
      
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
    async userlogin() {
      try {  
        await this.$store.dispatch('login', this.credit);
        // console.log(res.msg);
        this.userInfo();
      } catch (error) {  
        console.error('Error login:', error); 
      }
    },
    async userInfo() {
      try {
        await this.$store.dispatch('getUserInfo');
      } catch (error) {
        console.error('Error fetching info:', error);  
      }
    },
  }
}
</script>
