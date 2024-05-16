<template>
  <div id="app">
    <!-- TODO: 隐藏导航栏需要vuex，从长计议 -->
    <div id="nav" v-if="showNav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link> |
      <router-link to="/reader">Reader</router-link> |
      <router-link to="/Center">Center</router-link>
    </div>
    <router-view />
  </div>
</template>
<script>
export default {
  data() {
    return {
      showNav: false
    }
  }
}
</script>


<style lang="less">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
