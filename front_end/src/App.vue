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
  }
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
