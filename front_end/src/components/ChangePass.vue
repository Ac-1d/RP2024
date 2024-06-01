<template>
  <el-dialog
    :visible="changePassFlag"
    :color=pick
    :close-on-click-modal="false"
    :before-close="logdialogclose"
    :destroy-on-close="true"
  >
  <Menu></Menu>
    <el-form :model="loginForm" ref="loginFormRef" label-width="80px">
      <el-image :src="require('@/assets/log.png')"></el-image>
      <el-form-item label="电话">
        <el-input v-model="loginForm.tele"></el-input>
      </el-form-item>
      <el-form-item v-if='isRegister' label="用户名">
        <el-input v-model="loginForm.username"></el-input>
      </el-form-item>
      <el-form-item label="密码">
        <el-input v-model="loginForm.password" show-password></el-input>
      </el-form-item>
      <el-form-item v-if='isRegister' label="确认密码" >
        <el-input v-model="loginForm.password2" show-password></el-input>
      </el-form-item>

      <el-form-item>
        <el-button v-if='isRegister' type="primary" @click="submitForm">注册</el-button>
        <el-button type="primary" @click="logdialogclose">取消</el-button>
      </el-form-item>
    </el-form>
  </el-dialog>
</template>

<script>
import Menu from "@/components/Menu.vue"
export default {

  name: "ChangePass",
  props: {
    dialogflag: Boolean,
  },
  components: { Menu },
  emits: ['closedia'],
  data() {
    return {
      loginForm: {
        tele:'',
        username: '',
        password: '',
        password2: '',
      },
      isRegister: true,
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