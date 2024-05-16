<template>
  <div class="messages">
    <!-- 用户信息 -->
    <div class="info">
    <p>用户名：{{ myname }}</p>
    <p>ID-{{ myid }}</p>
    </div>
    <!-- 消息列表 -->
    <h6>收件箱</h6>
    <div class="recv">
      <div>
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
    </div>
    <!-- 发送消息板块 表单 -->
    <div class="send-message">
    </div>
  </div>
</template>

<script>
export default{
  name: "MessageBlock",
  props: {
    maxText: {
      type: Number, 
      default: 500
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
        {from: "0someone-foryou", title: "0xxx-foryou", date: "2024.5.16"},
        {from: "1someone-foryou", title: "1xxx-foryou", date: "2024.5.17"},
      ],
      // 收到的信息recvs: [{from: "someone-foryou", title: "xxx-foryou"}, ...],
      sends: [],
      // 已发送的信息send: [{to: "someone-sendto", title: "xxx-sendto"}, ...],
      drafts: [],
      // 草稿箱draft: [{to: "someone-draft", title: "xxx-draft"}, ...],
    }
    
  }
}</script>