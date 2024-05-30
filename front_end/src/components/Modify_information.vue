<template>
<div>
<el-drawer
  title="个人信息"
  :visible.sync="drawer"
  :direction="rtl"
  :before-close="handleClose">
  <div class="modify">
  <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">

  <el-form-item label="昵称" prop="NickName_k">
    <el-input v-model="ruleForm.NickName_k" ></el-input>
  </el-form-item>

  <el-form-item label="性别" prop="sex_k">
    <el-radio-group v-model="ruleForm.sex_k">
      <el-radio label="男"></el-radio>
      <el-radio label="女"></el-radio>
    </el-radio-group>
  </el-form-item>

  <el-form-item label="电话号码" prop="tele">
    <el-input v-model="ruleForm.tele" readonly></el-input>
  </el-form-item>

  <el-form-item label="出生日期" required>
    <el-col :span="11">
      <el-form-item prop="birth_k">
        <el-date-picker type="date" placeholder="请选择出生日期" v-model="ruleForm.birth_k" style="width: 150%;"></el-date-picker>
      </el-form-item>
    </el-col>
  </el-form-item>

  <el-form-item label="个性签名" prop="signature_k">
    <el-input v-model="ruleForm.signature_k"></el-input>
  </el-form-item>

  <div class="flex-container">
  <el-form-item label="密码" prop="password">
    <el-input v-model="ruleForm.password" type="password" readonly></el-input>
  </el-form-item>
  <el-button @click="setTrue">修改密码</el-button>
  </div>

  <div class="flex-container" v-if="isChange">
  <el-form-item label="请输入旧密码" prop="password_check">
    <el-input type="password" v-model="ruleForm.password_check" autocomplete="off"></el-input>
  </el-form-item>

  <el-form-item label="密码" prop="password_k">
    <el-input type="password" v-model="ruleForm.password_k" autocomplete="off"></el-input>
  </el-form-item>
  <el-form-item label="确认密码" prop="checkPass">
    <el-input type="password" v-model="ruleForm.checkPass" autocomplete="off"></el-input>
  </el-form-item>

  <el-button @click="setFalse">确认修改</el-button>
  </div>


</el-form>
  </div>
</el-drawer>
</div>
</template>


<script>
  export default {
    name:"Modify_info",
    props: {
        drawer:Boolean,
    },
    emits: ['closedia'],
    data() {
      return {
          ruleForm: {
          NickName: 'pizza_k',
          birth: new Date('2004-07-13'),
          sex: '女',
          tele: '15513107588',
          signature: '远方，就是我站立的地方',
          password: '59jkb2h0',
          ID:'2004010128',
          level:7,

          NickName_k: 'pizza_k',
          birth_k: new Date('2004-07-13'),
          sex_k: '女',
          signature_k: '远方，就是我站立的地方',
          password_check: '',
          password_k: '',
          password_k2: '',

        },
        isChangePass:false,
        rules: {
          NickName_k: [
            { required: true, message: '请输入昵称', trigger: 'blur' },
          ],
          birth_k: [
            { type: 'date', required: true, message: '请选择出生日期', trigger: 'change' }
          ],
          sex_k: [
            { required: true, message: '请选择性别', trigger: 'change' }
          ],

          signature_k: [
            { required: true, message: '请输入个性签名', trigger: 'blur' },
          ],

          password_check:[
            { required: true, message: '请输入旧密码', trigger: 'blur' },
            {
               validator: (rule, value, callback) => {
                  if (value !== this.ruleForm.password) {
                    callback(new Error('密码错误'));
                  } else {
                    callback();
                  }
               },
               trigger: 'blur'
            }

          ],

          password_k: [
            { required: true, message: '请输入新密码', trigger: 'blur' },
            { min: 8, max: 14, message: '密码长度为8-14位', trigger: 'blur' }
          ],
          password_k2: [
            { required: true, message: '请重新输入密码', trigger: 'blur' },
            {
               validator: (rule, value, callback) => {
                  if (value !== this.ruleForm.password_k) {
                    callback(new Error('两次输入密码不一致'));
                  } else {
                    callback();
                  }
               },
               trigger: 'blur'
            }

          ],

        }
      };

    },
    methods: {
      handleClose() {
        this.$confirm('确认关闭？')
          .then(() => {
            this.$emit('closedia');
          })
          .catch(() => {});
      },
      setTrue() {
         this.isChange = true;

      },
      setFalse() {
         this.isChange = false;
         this.$nextTick(() => {
           // 此处可以进行DOM操作或检查视图更新，但在这个例子中并不需要额外操作
         });
      }
    },
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            alert('submit!');
          } else {
            console.log('error submit!!');
            return false;
          }
        });
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      }


};
</script>

<style scoped>
.flex-container {
  display: flex;
  flex-direction: column; /* 修改为垂直布局 */
}
.modify {
  /* 重置或覆盖可能的文本对齐样式 */
  text-align: left !important;
  width:80%;
  /* 如果需要进一步精确控制输入框的位置，可以根据实际情况调整 */
}
</style>