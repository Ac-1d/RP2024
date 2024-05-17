<template>
  <div id="messages">
    <!-- 用户信息 -->
    <div id="info">
      <p>用户名：{{ myname }}</p>
      <p>ID-{{ myid }}</p>
      <nav>
        <a href="#" @click="page=0">写信</a><br/>
        <a href="#" @click="page=1">收信</a><br/>
        <a href="#" @click="page=2">已发送</a><br/>
        <a href="#" @click="page=3">草稿箱</a><br/>
      </nav>
    </div>
    <!-- 消息列表 -->
    <div id="content">
      <div v-if="page==0">
        <h1>写信</h1>
        <MyInput :maxLen="1000" v-model="content" name="发送"></MyInput>
        <p>内容是{{ content }}</p>
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
import MyInput from "@/components/MyInput.vue";
import MyTable from "@/components/MyTable.vue";

export default{
  name: "MessageBlock",
  components: {
    MyInput,
    MyTable
  },
  props: {
    maxText: {
      type: Number, 
      default: 2000
    },
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
      page: 1, 
      sendto: '',
      content: ''
    }
  }
}
</script>

<style scoped>
#messages{
  margin-bottom: 10px;
  #info {
    background-color:rgb(150, 255, 0);
    height:200px;
    width:100px;
    float:left;
  }
  #content {
    background-color:#EEEEEE;
    height:200px;
    width:200px;
    float:left;
  }
}
</style>