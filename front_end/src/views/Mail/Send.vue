<template>
  <div :style="{ width: windowWidth + 'px' }">
    <Mail/>
    <div style="float: right; 
    background-color: gainsboro; 
    height: 70px; width: 1200px;">
      <el-button style="float: left; font-family: 'Arial', sans-serif;
      width: 100px; margin: 15px 0px 0px 15px;" 
      @click="submitMessage">发送</el-button>

      <el-input style="float: left;  font-family: 'Arial', sans-serif;
      width: 1000px; margin: 15px 0px 0px 15px;" v-model="sendto" :maxlength="1000" placeholder="收件人"></el-input>
    </div>
    <div style="float: right; background-color: gainsboro; height: 960px; width: 1200px;">
      <el-input 
      type="textarea" 
      style="float: left; width: 1115px; margin: 0px 0px 0px 15px;" 
      :autosize="{ minRows: 20, maxRows: 25}" resize="none"
      v-model.trim="content" :maxlength="100000"
      placeholder="内容"></el-input>
    </div>
  </div>
</template>
<script>
import Mail from '@/views/Mail/Mail.vue';

export default{
  name: 'Send',
  data() {
    return {
      show: false,
      content: '',
      sendto: '',
      windowWidth: document.documentElement.clientWidth,  //实时屏幕宽度
      windowHeight: document.documentElement.clientHeight,   //实时屏幕高度
    }
  },
  components: {
    Mail,
  },
  methods: {
    submitMessage(){
      console.log('submit an Email')// 提交信件
    }
  },
  watch: {
    windowHeight (val) {
      let that = this;
      console.log("实时屏幕高度：",val, that.windowHeight );
    },
    windowWidth (val) {
      let that = this;
      console.log("实时屏幕宽度：",val, that.windowHeight );
    }
  },

  mounted() {
    var that = this;
    // <!--把window.onresize事件挂在到mounted函数上-->
    window.onresize = () => {
      return (() => {
        window.fullHeight = document.documentElement.clientHeight;
        window.fullWidth = document.documentElement.clientWidth;
        that.windowHeight = window.fullHeight;  // 高
        that.windowWidth = window.fullWidth; // 宽
      })()
    };
  }
}
</script>