<template>
  <el-dialog
    title="注册"
    :visible="dialogflag"

    :close-on-click-modal="false"
    :before-close="logdialogclose"
    :destroy-on-close="true"
  >

    <el-form :model="regisForm" :rules="rules" ref="regisForm" label-width="80px">
      <el-image :src="require('@/assets/log.png')"></el-image>
      <el-form-item label="电话" prop="tele">
        <el-input v-model="regisForm.tele"></el-input>
      </el-form-item>

      <el-form-item  label="用户名" prop="username">
        <el-input v-model="regisForm.username"></el-input>
      </el-form-item>

      <el-form-item label="密码" prop="password">
        <el-input v-model="regisForm.password" show-password></el-input>
      </el-form-item>
      <el-form-item  label="确认密码" prop="password2">
        <el-input v-model="regisForm.password2" show-password></el-input>
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="submitForm('regisForm')">注册</el-button>
        <el-button  @click="logdialogCancel('regisForm')">取消</el-button>
      </el-form-item>
    </el-form>
  </el-dialog>
</template>

<script>

export default {
  name: "Register_window",
  props: {
    dialogflag: Boolean,
  },

  emits: ['closedia'],
  data() {
    return {
      regisForm: {
        tele:'',
        username: '',
        password: '',
        password2: '',
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
         username : [
           { required: true, message: '请输入昵称', trigger: 'blur' },
         ],
         password: [
            { required: true, message: '请设置密码', trigger: 'blur' },
            { min: 8, max: 14, message: '密码长度为8-14位', trigger: 'blur' }
         ],
         password2: [
            { required: true, message: '请再次输入密码', trigger: 'blur' },
            {
               validator: (rule, value, callback) => {
                  if (value !== this.regisForm.password) {
                    callback(new Error('两次输入密码不一致'));
                  } else {
                    callback();
                  }
               },
               trigger: 'blur'
            }
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
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
            alert('提交成功!');
        }else{
            console.log('错误提交!!');
            return false;
        }
      });
    },
  },
};
</script>