<template>
  <div id="messages">
    <!-- 用户信息 -->
    <div class="side-nav">
      <p>用户名：{{ myname }}</p>
      <p>ID-{{ myid }}</p>
      <div class="side-nav-item"><a href="#" @click="page=0">写信</a></div>
      <div class="side-nav-item"><a href="#" @click="page=1">收信</a></div>
      <div class="side-nav-item"><a href="#" @click="page=2">已发送</a></div>
      <div class="side-nav-item"><a href="#" @click="page=3">草稿箱</a></div>
    </div>
    <!-- 消息列表 -->
    <div id="content">
      <div id="send" v-if="page==0">
        <h1>写信</h1>
        <SendMail/>
        <!-- 邮箱一般没有字数限制但是我不会写，就先加上 -->
        <!-- <p>内容是{{ content }}</p>调试用 -->
      </div><!-- 写信 -->
      <div v-else-if="page==1">
        <h1>收信</h1>
        <MyTable :rows="recvs"/>
      </div><!-- 收信 -->
      <div v-else-if="page==2">
        <h1>已发送</h1>
        <MyTable :rows="sends"/>
      </div><!-- 已发送 -->
      <div v-else-if="page==3">
        <h1>草稿箱</h1>
        <MyTable :rows="drafts"/>
      </div><!-- 草稿箱 -->
    </div>
    <!-- 发送消息板块 表单 -->
    <div id="send-message">
    </div>
  </div>
</template>

<script>
import MyTable from "@/components/MyTable.vue";
import SendMail from "@/components/SendMail.vue";

export default{
  name: "MessageBlock",
  components: {
    MyTable,
    SendMail
  },
  props: {
    myname: {
      type: String,
      default: '匿名'
    },
    myid: {
      type: Number,
      default: 0
    }
  },
  data() {
    return {
      recvs: [
        {from: "Lily", title: "Bills",    date: "2024-05-16 12:00:00"},
        {from: "Bill", title: "Business", date: "2024-05-17 18:30:00"},
      ], // 收到的信息recvs: [{from, title, datetime, read, content}],
      sends: [
        {to: 'Bob',    title:'Welcome',   date:"2024-11-16 12:00:00"},
        {to: 'Alice',  title:'Assignment',date:"2024-02-15 16:00:00"}
      ], 
      drafts: [], 
      page: 0, 
      sendto: '',
      content: ''
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
#messages{
  margin-bottom: 10px;
  /* 侧边栏 */
  .side-nav {
    font-weight: bold;
    color:#EEEEEE;
    position: fixed;
    top: 50%;
    right: 0;
    transform: translateY(-50%);
    background: rgba(0, 0, 0, 0.7);
    border-radius: 10px 0 0 10px;
    padding: 10px;
    z-index: 1000;
  }
  .side-nav-item {
    a{
      color: #EEEEEE;
      text-decoration: none;
    }
    text-align: center;
    color: white;
    padding: 10px;
    margin: 5px 0;
    cursor: pointer;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 5px;
    transition: background-color 0.3s, color 0.3s;
  }
  .side-nav-item:hover {
    background: #007bff;
    color: #fff;
  }
}
#content {
  background-color:#EEEEEE;
  width: 100%;
  height: 100%;
  float:left; 
  table {
    width: 80%;
  };
  th {
    width: 30%;
  };
  table, th, td {
    border: 1px black solid;
    border-collapse: collapse;
  }
  #send {
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
}
</style>