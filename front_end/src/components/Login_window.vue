<template>
  <el-dialog
    title="登录"
    :visible="dialogflag"

    :close-on-click-modal="false"
    :before-close="logdialogclose"
    :destroy-on-close="true"
  >

    <el-form :model="logForm" :rules="rules" ref="logForm" label-width="80px">
      <el-image :src="require('@/assets/log.png')"></el-image>
      <el-form-item label="用户名" prop="username">
        <el-input v-model="logForm.username" autocomplete="off"></el-input>
      </el-form-item>


      <el-form-item label="密码" prop="password">
        <el-input v-model="logForm.password" show-password></el-input>
      </el-form-item>


      <el-form-item>
        <el-button type="primary" @click="submitForm('logForm')">登录</el-button>
        <el-button  @click="logdialogCancel('logForm')">取消</el-button>

      </el-form-item>
    </el-form>
  </el-dialog>
</template>

<script>

export default {
  name: "Login_window",
  props: {
    dialogflag: Boolean,
  },

  emits: ['closedia'],
  data() {
    return {
      logForm: {
        username:'',
        password: '',
      },
      rules :{
         username: [
            { required: true, message: '请输入用户名', trigger: 'blur' },

         ],

         password: [
            { required: true, message: '请输入密码', trigger: 'blur' },
            { min: 8, max: 14, message: '密码长度为8-14位', trigger: 'blur' }
         ],

      },
    };
  },
  methods: {
    logdialogCancel(formName) {
      this.$confirm('确认关闭？')
          .then(() => {
               this.$refs[formName].resetFields();
               this.$emit('closedia');
          })
          .catch(() => {});
    },
    logdialogclose() {
       this.$confirm('确认关闭？')
           .then(() => {
               console.log('close');
               this.logForm.username='',
               this.logForm.password= '',
               this.$emit('closedia');
           })
           .catch(() => {});
    },



    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
            const userData = {
              username:this.logForm.username,
              password:this.logForm.password,
            };
            this.$store.dispatch('login',userData);

            this.$refs[formName].resetFields();
            this.$emit('closedia');

        }else{
            console.log('信息错误!!');
            return false;
        }
      });
    },
  },
};
</script>