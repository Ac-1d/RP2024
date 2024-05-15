<template>
  <div class="comment">
    <CommentBlock :maxText="600" myname="李正阳"/>
  </div>
</template>

<script>
import CommentBlock from "@/components/CommentBlock.vue";
export default {
  name: "Comments",
  components: {
    CommentBlock
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

    // text: this.newCommentText, 
    // author: this.myname, 
    // showReply: false,
    // likes: 0, 
    // replyText: '',
    // replies: []
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
</style>