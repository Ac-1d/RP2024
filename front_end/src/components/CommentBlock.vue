<template>
  <div class="comments">
    <!-- 评论显示 -->
    <div v-for="(comment, index) in comments" :key="index" class="comment">
      <!-- 循环显示的每条评论 -->
      <div class="single-comment">
        <h6>{{ comment.author }}:</h6>
        <p>{{ comment.text }} 赞：{{ comment.likes }}</p>
        <button @click="likeComment(index)">点赞</button>
        <button @click="deleteComment(index)">删除</button>
        <button @click="showReply(index)">展开</button>
        <button @click="beginReply(index)">回复</button>
      </div>
      <!-- 回复区 -->
      <div v-if="comment.showReply" class="sub-comment">  
        <!-- 回复显示 -->
        <div v-for="(reply, replyIndex) in comment.replies" :key="replyIndex" class="reply">  
          <p>{{ reply.text }} - {{ reply.author }}</p>  
        </div>  
      </div>
    </div>
    <!-- 评论、回复框 -->
    <div class="comment-box">
      <form @submit.prevent="addComment">
        <textarea v-model="newCommentText" placeholder="输入你的评论..."  
        @input="checkCommentLength"></textarea>
        <p>剩余字数 {{ remainingText }}</p>
        <p v-if="replying">正在回复 {{ comments[replyIndex].author }}</p>
        <!-- 返回评论 -->
        <button v-if="replying" @click="endReply()">返回评论</button>
        <button type="submit" :disabled="commentLengthExceeded">提交</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "CommentBlock",
  data() {
    return {
      comments: [
        { 
          text: '这是一条评论', 
          author: '张三', 
          likes: 0, 
          showReply: false,
          replyText: '',
          replies: [{text:'你好', author:'李正阳'},],
        },
        // 更多评论...  
        // 可以通过后端，从数据库中调用
      ],
      newCommentText: '',
      maxText: 10,
      commentLengthExceeded: false,
      replying: false,
      replyIndex: 0,
      myname: '匿名'
      // 当前用户名
    };
  },
  computed: {
    remainingText(){
      return this.maxText-this.newCommentText.length;
    }
  },
  methods: {
    addComment() {
      if (this.newCommentText) {
        if (this.replying) {
          const newReply = {
            text: this.newCommentText, 
            author: this.myname
          };
          this.comments[this.replyIndex].replies.push(newReply);
          this.endReply();
        }
        else {
          const newComment = { 
            text: this.newCommentText, 
            author: this.myname, 
            showReply: false,
            likes: 0, 
            replyText: '',
            replies: []
          };
          this.comments.push(newComment);
        }
        this.newCommentText = '';
      }
    },
    checkCommentLength() {  
      this.commentLengthExceeded = this.newCommentText.length > this.maxText;  
    },  // 检查评论的长度，不能超过maxText
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
    },
    beginReply(index){
      this.replyIndex=index;
      this.replying=true;
    },
    endReply(){
      this.replyIndex=0;
      this.replying=false;
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