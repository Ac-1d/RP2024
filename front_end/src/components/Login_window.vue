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
      <el-form-item label="用户名" prop="mobile">
        <el-input v-model="logForm.mobile" autocomplete="off"></el-input>
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
        mobile:'',
        password: '',
      },
      rules :{
         mobile: [
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
               this.logForm.mobile='',
               this.logForm.password= '',
               this.$emit('closedia');
           })
           .catch(() => {});
    },

    async getUserInfo() {

    },

    submitForm(formName) {
      this.$refs[formName].validate(async (valid) => {
        if (valid) {
            const userData = {
              mobile:this.logForm.mobile,
              password:this.logForm.password,
            };
            this.$refs[formName].resetFields();

            await this.$store.dispatch('login',userData);
            await this.$store.dispatch('getUserInfo');
            console.log('submit');
            console.log(this.$store.getters.userInfo);
            
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

