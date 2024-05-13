<template>
  <div>
    <div v-for="(comment, index) in comments" :key="index" class="comment">
      <h6>{{ comment.author }}:</h6>
      <p>{{ comment.text }} 赞：{{ comment.likes }}</p>
      <button @click="likeComment(index)">点赞</button>
      <button @click="deleteComment(index)">删除</button>
      <button @click="showReply(index)">评论</button>
      <div v-if="comment.showReply" class="sub-comment">  
        <form @submit.prevent="addReply(index, $event)">  
          <input type="text" v-model="comment.replyText" placeholder="输入你的回复...">  
          <button type="submit">提交</button>  
        </form>  
        <div v-for="(reply, replyIndex) in comment.replies" :key="replyIndex" class="reply">  
          <p>{{ reply.text }} - {{ reply.author }}</p>  
        </div>  
      </div>
    </div>

    <form @submit.prevent="addComment">
      <input type="text" v-model="newCommentText" placeholder="输入你的评论...">
      <button type="submit">提交</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      comments: [
        { 
          text: '这是一条评论', 
          author: '张三', 
          likes: 0, 
          showReply: false,
          replyText: '',
          replies: [{text:'你好', author:'李正阳'},]
        },
        // 更多评论...  
        // 可以通过后端，从数据库中调用
      ],
      newCommentText: '',
      myname: '匿名'
      // 当前用户名
    };
  },
  methods: {
    addComment() {
      if (this.newCommentText) {
        const newComment = { 
          text: this.newCommentText, 
          author: this.myname, 
          showReply: false,
          likes: 0, 
          replyText: '',
          replies: []
        };
        this.comments.push(newComment);
        this.newCommentText = '';
      }
    },
    likeComment(index) {
      if (index < this.comments.length && index >= 0) {
        this.comments[index].likes++;
      }
    },
    deleteComment(index) {  
      if (index < this.comments.length && index >= 0) {  
        this.comments.splice(index, 1);  
      }  
    },
    showReply(index) {
      if (index < this.comments.length && index >= 0) {  
        this.comments[index].showReply = !(this.comments[index].showReply);
      }  
    },
    addReply(index, event) {
      if (index < this.comments.length && index >= 0 && this.comments[index].replyText) {  
        const newReply = {
          text: this.comments[index].replyText,  
          author: this.myname,  
        };
        this.comments[index].replies.push(newReply);  
        this.comments[index].replyText = ''; // 清空输入框  
      }  
      // 阻止表单默认的提交行为  
      event.preventDefault();  
    }
  }
};  
</script>

<style scoped>
.comment {
  margin-bottom: 10px;
  /* 其他样式... */
}
</style>