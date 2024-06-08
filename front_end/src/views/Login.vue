<template>
  <div>
    <h1>我是登录界面</h1>
    <el-button type="text" @click="showLogdialog">登录</el-button>
    <Login_window :dialogflag="logvisible" @closedia="closeDialog"></Login_window>
  </div>
</template>

<script>
import Login_window from "@/components/Login_window.vue"

export default {
  name: 'Login',
  components: { Login_window },
  data() {
    return {
      logvisible: false, // Boolean 用于dialog隐藏/显示
    };
  },
  methods: {
    showLogdialog() {
      this.logvisible = true;
      // 可以在此处添加更多登录逻辑
    },
    closeDialog() {
      this.logvisible = false;
    },

  },
};
</script>