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
      <el-form-item label="电话" prop="mobile">
        <el-input v-model="logForm.mobile" autocomplete="off"></el-input>
      </el-form-item>


      <el-form-item label="密码" prop="password">
        <el-input v-model="logForm.password" show-password></el-input>
      </el-form-item>


      <el-form-item>
        <el-button type="primary" @click="submitForm('logForm')">登录</el-button>
        <el-button  @click="logdialogclose">取消</el-button>

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
  watch: {
    // 使用 watch 来监视 dialogflag 的变化
    dialogflag(newValue, oldValue) {
      // 当 dialogflag 的值发生变化时，这个函数会被调用
      console.log('dialogflag 的值从', oldValue, '变成了', newValue);
    },
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
        this.$emit('closedia');
    },

    submitForm(formName) {
      this.$refs[formName].validate(async (valid) => {
        if (valid) {
            const userData = {
              mobile:this.logForm.mobile,
              password:this.logForm.password,
            };
            this.$refs[formName].resetFields();

            const ans = await this.$store.dispatch('login',userData);
            console.log('ans'+ans.msg);

            if(ans.msg === '登录成功'){
                await this.$store.dispatch('getUserInfo');
                this.$emit('closedia');
            }else{
                alert("用户不存在或密码错误");
            }

        }else{
            console.log('信息错误!!');
            return false;
        }
      });
    },
  },
};
</script>