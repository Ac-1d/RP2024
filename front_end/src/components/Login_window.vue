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
      <el-form-item label="电话" prop="tele">
        <el-input v-model="logForm.tele" autocomplete="off"></el-input>
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
        tele:'',
        password: '',
      },
      rules :{
         tele: [
            { required: true, message: '请输入电话号码', trigger: 'blur' },
            {
                pattern: /^1[3-9]\d{9}$/, // 中国手机号正则，以1开头，第二位是3-9之间的数字，后面跟9位数字
                message: '请输入正确的电话号码格式',
                trigger: ['blur', 'change'] // 触发验证的时机，这里设定为失去焦点或值变化时
            }

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
               this.logForm.tele='',
               this.logForm.password= '',
               this.$emit('closedia');
           })
           .catch(() => {});
    },

    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
            const userData = {
              mobile:this.logForm.tele,
              password:this.logForm.password,
            };

            const ans = this.$store.dispatch('login',userData);
            console.log("得到ans:"+ans);
            this.userInfo();
        }else{
            console.log('信息错误!!');
            return false;
        }
      });
    },
    async userInfo() {
      try {
        await this.$store.dispatch('getUserInfo');
      } catch (error) {
        console.error('Error fetching info:', error);
      }
    },
  },
};
</script>