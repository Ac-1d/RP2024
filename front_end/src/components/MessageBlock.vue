<template>
  <div class="messages">
    <!-- 用户信息 -->
    <div class="info">
    <p>用户名：{{ myname }}</p>
    <p>ID-{{ myid }}</p>
    </div>
    <!-- 消息列表 -->
    <div class="message">
      <div>
        <!-- 单条信息显示  -->
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
      default: -1
    }
  }
}</script>