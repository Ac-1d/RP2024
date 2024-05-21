<template>
  <div id="send">
    <div id="div1">
      <button class="button" @clicked="submitMessage" type="submit">发送</button>
      <input class="input" v-model="sendto" placeholder="收件人"
      @input="sendto=sendto.substring(0,127)">
    </div>
    <div id="div2">
      <textarea class="input" v-model="content" placeholder="内容"
      @input="content=content.substring(0,32768)">
      </textarea>
    </div>
  </div>
</template>

<script>
export default{
  name: "SendMail",
  data() {
    return {
      content:'',
      sendto:''
    }
  },
  methods: {
    submitMessage(){
      console.log('submit an Email')// 提交信件
    }
  }
}
</script>

<style scoped>
.input {
  resize: none;
  margin: 0 0 1% 1%;
  float: left;
  background-color: white;
  border: none;
  border-radius: 4px;
  color: black;
  width: 83%;
  height: 1%;
  padding: 1% 1%;
  text-align: left;
  text-decoration: none;
  font-size: 16px;
  font-weight: 1000;
  box-shadow: 1px;
}
.button {
  margin: 0 0 1% 1%;
  float: left;
  background-color: grey;
  border: none;
  border-radius: 4px;
  color: white;
  width: 5%;
  height: 1%;
  padding: 1% 1%;
  text-align: center;
  text-decoration: none;
  font-size: 16px;
  font-weight: 1000;
  box-shadow: 1px;
  transition: background-color 0.3s, color 0.3s;
}
.button:hover {
  background: #007bff;
  color: #fff;
}
.send {
  #div1 {
    input {
      width: 80%
    }
  }
  #div2 {
    textarea {
      width: 86%;
      height: 390px;
      font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
  }
}
</style>