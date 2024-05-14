<template>
  <div class="comments">
    <CommentBlock :maxText="20" myname="Yining"/>
  </div>
</template>

<script>
import CommentBlock from "@/components/CommentBlock.vue";
export default {
  name: "Comments",
  components: {
    CommentBlock
  }
};
CommentBlock.comments = [
  { 
    text: '这是一条评论', 
    author: '张三', 
    likes: 0, 
    showReply: false,
    replyText: '',
    replies: [{text:'你好', author:'李正阳'},],
  },
  // 更多评论...  
  // 可以通过后端暴露的接口，从数据库中调用
];
</script>

<style scoped>
.comment {
  margin-bottom: 10px;
  /* 其他样式... */
}
</style>