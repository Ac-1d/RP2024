<template>
<div>

<el-drawer
  title="个人信息"
  :visible.sync="drawer"
  :direction="rtl"
  :before-close="handleClose">
  <div class="modify">
  <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">

  <el-form-item label="ID" prop="ID">
    <el-input v-model="ruleForm.ID" readonly></el-input>
  </el-form-item>

  <el-form-item label="昵称" prop="NickName_k">
    <el-input v-model="ruleForm.NickName_k" ></el-input>
  </el-form-item>

  <el-form-item label="Level" prop="level">
    <el-input v-model="ruleForm.level" readonly></el-input>
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
    <el-input v-model="ruleForm.signature_k" type="textarea" :rows="2"></el-input>
  </el-form-item>

  <el-form-item label="密码" prop="password" style="width: 150%;">
    <el-input v-model="ruleForm.password" type="password" style="width: 50%;" readonly></el-input>
    <el-button class="borderless-btn" @click="setTrue" style="margin-right: auto;">修改密码</el-button>
  </el-form-item>

  <el-form-item>
    <el-button type="primary" @click="submitForm('ruleForm')">提交</el-button>
    <el-button @click="resetForm('ruleForm')">重置</el-button>
  </el-form-item>

 </el-form>


  <el-form v-if="isChange" :model="ruleForm1" :rules="rules1" ref="ruleForm1" label-width="100px" class="demo-ruleForm1">
  <el-form-item label="旧密码" prop="password_check">
    <el-input  v-model="ruleForm1.password_check" autocomplete="off"></el-input>
  </el-form-item>
  <el-form-item label="新密码" prop="password_k">
    <el-input  type="password" v-model="ruleForm1.password_k" autocomplete="off"></el-input>
  </el-form-item>

  <el-form-item label="确认密码" prop="password_k2" style="width: 150%;">
    <el-input type="password" v-model="ruleForm1.password_k2" autocomplete="off" style="width: 50%;"></el-input>
    <el-button class="borderless-btn"  @click="submitPass('ruleForm1')" style="margin-right: auto;">确认修改</el-button>
  </el-form-item>

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
          tele: '15513107588',
          password: '59jkb2h0',
          ID:'2004010128',
          level:7,

          NickName_k: 'pizza_k',
          birth_k: new Date('2004-07-13'),
          sex_k: '女',
          signature_k: '远方，就是我站立的地方',
        },
        ruleForm1:{
          password_check: '',
          password_k: '',
          password_k2: '',
        },
        isChange:false,
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

        },
        rules1: {
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
                  if (value !== this.ruleForm1.password_k) {
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
      },
      submitForm(formName) {
        if(this.isChange){
            alert('密码修改仍然未完成!!');
            return;
        }
        this.$refs[formName].validate((valid) => {
          if (valid) {
            alert('提交成功!');
          } else {
            console.log('错误提交!!');
            return false;
          }
        });
      },
      submitPass(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            alert('修改密码成功');
            this.setFalse();
            this.ruleForm1.password_check='';
            this.ruleForm1.password_k='';
            this.ruleForm1.password_k2='';
            console.log(this.isChange);
          } else {
            console.log('修改密码失败，存在错误!!');
            return false;
          }
        });
      },

      resetForm(formName) {
        this.$refs[formName].resetFields();
      }
    },
};
</script>

<style scoped>

.modify {
  /* 重置或覆盖可能的文本对齐样式 */
  text-align: left !important;
  width:80%;
  /* 如果需要进一步精确控制输入框的位置，可以根据实际情况调整 */
}
.borderless-btn {
  border: none; /* 移除边框 */
  background-color: transparent; /* 设置背景透明，如果需要完全透明的背景 */
  outline: none; /* 移除轮廓，以避免焦点时显示的虚线边框 */
}
</style>