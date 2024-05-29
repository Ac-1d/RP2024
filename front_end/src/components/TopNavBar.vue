<template>
  <div class="top-nav-bar" v-if="showNavBar">
    <div class="left-links">
      <router-link to="/">Home</router-link>
      <router-link to="/about">About</router-link>
      <router-link to="/reader">Reader</router-link>
      <router-link to="/creation">创作中心</router-link>
    </div>
    <div class="right-links">
      <router-link to="/login">登录</router-link>
      <router-link to="/register">注册</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "TopNavBar",
  data() {
    return {
      showNavBar: true
    }
  }
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
</style>
