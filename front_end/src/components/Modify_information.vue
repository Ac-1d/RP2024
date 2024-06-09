<template>
<div>

<el-drawer
  title="个人信息"
  :visible.sync="drawer"

  :before-close="handleClose">
  <div class="modify">

  <el-form :model="tempRuleForm" :rules="rules" ref="tempRuleForm" label-width="100px" class="demo-ruleForm">

  <el-form-item label="ID" prop="ID">
    <el-input v-model="tempRuleForm.ID" readonly></el-input>
  </el-form-item>

  <el-form-item label="昵称" prop="nickName">
    <el-input v-model="tempRuleForm.nickName" ></el-input>
  </el-form-item>

  <el-form-item label="Level" prop="level">
    <el-input v-model="tempRuleForm.level" readonly></el-input>
  </el-form-item>

  <el-form-item label="性别" prop="sex">
    <el-radio-group v-model="tempRuleForm.sex">
      <el-radio label="男"></el-radio>
      <el-radio label="女"></el-radio>
    </el-radio-group>
  </el-form-item>

  <el-form-item label="电话号码" prop="tele">
    <el-input v-model="tempRuleForm.tele" readonly></el-input>
  </el-form-item>

  <el-form-item label="出生日期" required>
    <el-col :span="11">
      <el-form-item prop="birth">
        <el-date-picker type="date" placeholder="请选择出生日期" v-model="tempRuleForm.birth" style="width: 150%;"></el-date-picker>
      </el-form-item>
    </el-col>
  </el-form-item>

  <el-form-item label="个性签名" prop="signature">
    <el-input v-model="tempRuleForm.signature
    " type="textarea" :rows="2"></el-input>
  </el-form-item>

  <el-form-item label="密码" prop="password" style="width: 150%;">
    <el-input v-model="tempRuleForm.password" type="password" style="width: 50%;" readonly></el-input>
    <el-button class="borderless-btn" @click="setTrue" style="margin-right: auto;">修改密码</el-button>
  </el-form-item>

  <el-form-item>
    <el-button type="primary" @click="submitForm('tempRuleForm')">提交</el-button>
    <el-button @click="handleClose">取消</el-button>
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
    <!--<el-button class="borderless-btn"  @click="submitPass('ruleForm1')" style="margin-right: auto;">确认修改</el-button>-->
  </el-form-item>

  <el-form-item class="borderless-btn">
    <el-button type="primary" @click="submitPass('ruleForm1')">确认修改</el-button>
    <el-button @click="resetPass('ruleForm1')">放弃修改</el-button>
  </el-form-item>


  </el-form>



 </div>
</el-drawer>

</div>
</template>


<script>
import axios from 'axios';
  export default {
    name:"Modify_info",
    props: {
        drawer:Boolean,
        ruleForm: {
           type: Object,
           required: true
        },
    },
    emits: ['closedia','send'],
    data() {
      return {
        tempRuleForm: { ...this.ruleForm },
        ruleForm1:{
          password_check: '',
          password_k: '',
          password_k2: '',
        },
        isChange:false,
        rules: {
          nickName: [
            { required: true, message: '请输入昵称', trigger: 'blur' },
            { max: 14, message: '昵称最长为14位', trigger: 'blur' }
          ],
          birth: [
            { type: 'date', required: true, message: '请选择出生日期', trigger: 'change' }
          ],
          sex: [
            { required: true, message: '请选择性别', trigger: 'change' }
          ],

          signature: [
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
   watch: {
    ruleForm: {
      deep: true, // 深度监视，以便监视嵌套对象的变化
      handler(newVal) {
        this.tempRuleForm = { ...newVal };
        console.log('modi'+this.tempRuleForm.nickName);
      },
    },
  },
    methods: {
      handleClose() {
        this.$confirm('确认关闭？')
          .then(() => {
            this.resetForm("tempRuleForm");
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
            console.log(this.ruleForm);

            alert('提交成功!');
            this.commitInfo();
            this.$emit('closedia');
            this.$emit('send',this.tempRuleForm);

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
            this.tempRuleForm.password = this.ruleForm1.password_k;
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
        console.log(this.$refs[formName]);
      },

      resetPass(formName) {
        this.$refs[formName].resetFields();
        this.setFalse();
      },

      commitInfo: async function() {
        console.log('start');
        let formData = new FormData();
        formData.append('username', this.tempRuleForm.nickName);
        let gender = 0;
        if(this.tempRuleForm.sex === "女"){
            gender = 1;
        }
        formData.append('gender', gender);
        formData.append('password', this.tempRuleForm.password);
        // formData.append('user_icon', this.userInfo.avatar_path);
        let datetimeForDB = this.tempRuleForm.birth.toISOString().replace('Z', '').slice(0, 19);
        formData.append('birth_date', datetimeForDB);
        formData.append('signature', this.tempRuleForm.signature);
        console.log(formData);
        try {
            const response = await axios.patch(`/users/register?user_id=${this.$store.state.userInfo.id}`, formData);
            console.log('try');
            if (response.status === 200 && response.data.message === '用户信息更新成功') {
                console.log(response.data.message);

                // 在此处处理成功更新的结果，例如通知用户或刷新列表
            } else {
                console.error('更新失败');
            }
        } catch (error) {
            console.error(error);
        }
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