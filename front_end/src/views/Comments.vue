<template>
  <div>
    <div class="comment">
      <CommentBlock :myid="100" myname="李正阳"/>
    </div>
    <div class="message">
      <MessageBlock />
    </div>
  </div>
</template>

<script>
import CommentBlock from "@/components/CommentBlock.vue";
import MessageBlock from "@/components/MessageBlock.vue";
export default {
  name: "Comments",
  components: {
    CommentBlock,
    MessageBlock
  },
  data() {
    return {
      name: '李正阳'
    }
  }
};
CommentBlock.comments = [
  { 
    text: '这是一条评论', 
    author: '张三', 
    likes: 0,
    showReply: false, // 仅限网页的属性
    replyText: '', // 仅限网页的属性
    replies: [{text:'你好', author:'李正阳'},],
  },
  // 更多评论...  
  // 可以通过后端暴露的接口，从数据库中调用
];
</script>

<style scoped>
.comment {
  margin-bottom: 10px;
  width: 200px;
  float: left;
  background-color: rgb(0, 213, 255);
  /* 其他样式... */
}
.message {
  margin-bottom: 10px;
  width: 300px;
  float: right;
  background-color: rgb(174, 255, 0);
}
</style>