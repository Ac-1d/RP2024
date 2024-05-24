<template>
  <el-dialog
    title="用户登录"
    :visible="dialogflag"
    :close-on-click-modal="false"
    :before-close="logdialogclose"
    :destroy-on-close="true"
  >
  <Menu></Menu>
    <el-form :model="loginForm" ref="loginFormRef" label-width="80px">
      <el-image :src="require('@/assets/log.png')"></el-image>
      <el-form-item label="用户名">
        <el-input v-model="loginForm.username"></el-input>
      </el-form-item>
      <el-form-item label="密码">
        <el-input v-model="loginForm.password" show-password></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm">登录</el-button>
      </el-form-item>
    </el-form>
  </el-dialog>
</template>

<script>
import Menu from "@/components/Menu.vue"
export default {

  name: "Login_window",
  props: {
    dialogflag: Boolean,
  },
  components: { Menu },
  emits: ['closedia'],
  data() {
    return {
      loginForm: {
        username: '',
        password: '',
      },
    };
  },
  methods: {
    logdialogclose() {
      this.$emit('closedia');
    },
    submitForm() {
      // 实现登录逻辑
    },
  },
};
</script>