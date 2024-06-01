<template>
  <el-container class="layout-middle">
    <el-header style="height: 0px;">
    </el-header>
    <el-main>
      <el-form>
        <el-form-item>
          <el-button style="float: left; display: flex; margin-top: 20px;" type="primary"
          @click="submitMessage" show-word-limit>发送</el-button>
          <el-button style="float: left; display: flex; margin-top: 20px;" type="primary"
          @click="draft" show-word-limit>存入草稿</el-button>
        </el-form-item>
        <el-form-item>
          <el-input style="float: left; display: flex;" v-model="sendto" 
          :maxlength="1000" placeholder="收件人账号" clearable></el-input>
        </el-form-item>
        <el-form-item><el-input style="float: left; display: flex;" v-model="title" 
            :maxlength="1000" placeholder="主题" clearable></el-input></el-form-item>
        <el-form-item>
          <el-input
          type="textarea" style="resize:none;"
          :autosize="{ minRows: 10, maxRows: 30}"
          placeholder="请输入内容" clearable
          v-model.trim="content" :maxlength="100000"></el-input>
        </el-form-item>
        <el-form-item>
          <el-upload
            class="upload-demo"
            drag
            action="#"
            multiple>
            <i class="el-icon-upload"></i>
            <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
            <!-- <div class="el-upload__tip" slot="tip">上传文件不超过500kb</div> -->
          </el-upload>
        </el-form-item>
      </el-form>
    </el-main>
  </el-container>
</template>
<script>
import {currentTime} from '@/js/Time.js';
export default{
  name: 'Send',
  props: {
    Info: {
      type: Number,
      default: 0,
    }
  },
  data() {
    return {
      content: '',
      sendto: '',
      title: '',
    }
  },
  components: {
  },
  methods: {
    submitMessage(){
      console.log('submit an Email')// 提交信件
    },
    draft(){
      // console.log('drafting');
      let data = {
        sendto: this.sendto,
        content: this.content,
        title: this.title,
        time: currentTime(),
      };
      this.$emit('draft', data);
    }
  },
  created(){
    if(this.Info != 0){
      this.sendto = '' + this.Info;
    }
    console.log(this.Info);
  }
}
</script>