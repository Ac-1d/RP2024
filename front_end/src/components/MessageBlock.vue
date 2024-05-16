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
        <textarea v-model="sendto" @input="checkExeed(100)"></textarea>
        <textarea v-model="content" @input="checkExeed(2000)"></textarea>
        <button type="submit" :disabled="mailLengthExceeded">提交</button>
      </div>
      <div v-else-if="page==1">
        <h1>收信</h1>
        <table>
          <thead> 
            <!-- 表头 -->
            <tr>
              <th>发件人</th>
              <th>标题</th>
              <th>日期</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(recv, index) in recvs" :key="index">
              <td>{{ recv.from }}</td>
              <td>{{ recv.title }}</td>
              <td>{{ recv.date }}</td>
            </tr>
          </tbody>
        </table>
        <!-- 发信人from 主题title 是否已读 -->
        <!-- 通过v-for来实现显示 -->
      </div>
      <div v-else-if="page==2">
        <h1>已发送</h1>
      </div>
      <div v-else-if="page==3">
        <h1>草稿箱</h1>
      </div>
    </div>
    <!-- 发送消息板块 表单 -->
    <div id="send-message">
    </div>
  </div>
</template>

<script>
export default{
  name: "MessageBlock",
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
    },
    content: String
  },
  data() {
    return {
      recvs: [
        {from: "0someone-foryou", title: "0xxx-foryou", date: "2024-05-16 12:00:00"},
        {from: "1someone-foryou", title: "1xxx-foryou", date: "2024-05-17 18:30:00"},
      ], // 收到的信息recvs: [{from, title, datetime, read, content}],
      sends: [], 
      drafts: [], 
      page: 1, // 写信0，收信1，发件箱2，草稿箱3，默认收信
      mailLengthExceeded: false,
      sendto: ''
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