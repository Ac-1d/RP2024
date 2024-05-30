<template>
  <el-container>
    <el-header>
      <el-container>
        <el-aside style="width: auto; " >
          <el-button style="float: left; display: flex; margin-top: 20px;"
          @click="submitMessage" show-word-limit>发送</el-button>
        </el-aside>
        <el-main>
          <el-input style="float: left; display: flex;" v-model="sendto" 
          :maxlength="1000" placeholder="收件人账号">
          </el-input>
        </el-main>
      </el-container>
    </el-header>
    <el-main>
      <el-input
        type="textarea" style="resize:none;"
        :autosize="{ minRows: 10, maxRows: 30}"
        placeholder="请输入内容" 
        v-model.trim="content" :maxlength="100000">
      </el-input>
    </el-main>
    <el-main>
      <el-container>
        <el-upload
          class="upload-demo"
          drag
          action="#"
          multiple>
          <i class="el-icon-upload"></i>
          <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
          <div class="el-upload__tip" slot="tip">上传文件不超过500kb</div>
        </el-upload>
      </el-container>
    </el-main>
  </el-container>
</template>
<script>

export default{
  name: 'Send',
  data() {
    return {
      show: false,
      content: '',
      sendto: '',
    }
  },
  components: {
  },
  methods: {
    submitMessage(){
      console.log('submit an Email')// 提交信件
    }
  },
}
</script>