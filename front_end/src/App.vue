<template>
  <div id="app">
    <!-- 顶级导航栏 -->
    <TopNavBar />
    <router-view />
  </div>
</template>

<script>
import TopNavBar from "@/components/TopNavBar.vue";

export default {
  name: "App",
  components: {
    TopNavBar
  },
  // 防止刷新时页面信息被清空;保存用户名及token
  created () {
    // 在页面加载时读取sessionStorage里的状态信息
    if (sessionStorage.getItem('store')) {
      this.$store.replaceState(
        Object.assign(
          {},
          this.$store.state,
          JSON.parse(sessionStorage.getItem('store'))
        )
      )
    } // 在页面刷新时将vuex里的信息保存到sessionStorage里 // beforeunload事件在页面刷新时先触发

    window.addEventListener('beforeunload', () => {
      sessionStorage.setItem('store', JSON.stringify(this.$store.state))
    })
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
