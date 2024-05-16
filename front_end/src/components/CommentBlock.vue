<template>
  <div class="comments">
    <!-- 用户信息 -->
    <div class="info">
      <p>用户名：{{ myname }}</p>
      <p>ID-{{ myid }}</p>
    </div>
    <!-- 评论显示 -->
    <div v-for="(comment, index) in comments" :key="index" class="comment">
      <!-- 循环显示的每条评论 -->
      <div>
        <h6>{{ comment.author }}:</h6>
        <p>{{ comment.text }} 赞：{{ comment.likes }}</p>
        <p>{{ comment.currentTime }}</p>
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
        <!-- 显示正在回复给某人 -->
        <p v-if="replying">正在回复 {{ comments[replyIndex].author }}</p>
        <!-- 退出回复，返回评论 -->
        <button v-if="replying" @click="endReply()">返回评论</button>
        <button type="submit" :disabled="commentLengthExceeded">提交</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "CommentBlock",
  props: {
    maxText: {
      type: Number, // 指定这个 prop 是数字类型
      default: 500 // 默认值 500
    },
    myname: {
      type: String,
      default: '匿名'
    },
    myid: {
      type: Number,
      default: 100
      // 默认id暂定为0
    }
  },
  data() {
    return {
      comments: [],
      newCommentText: '',
      commentLengthExceeded: false,
      replying: false,
      replyIndex: 0,
      // 当前用户名
    };
  },
  computed: {
    remainingText(){
      return this.maxText-this.newCommentText.length;
    }
  },
  methods: {
    getChildData() {
      return this.data;
    },// 试图加上getter供外部获取数据，暂时不起作用
    setComment(inData) {
      this.comments = inData;
    },// 试图让这个函数来在外部加上已有评论，但是暂不起作用
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
            replies: [],
            currentTime: new Date()
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
.comments {
  margin-bottom: 10px;
  .comment {
    position: float;
    top: 200px;
    bottom: 200px;
  } 
  /* 这里固定评论显示区的位置；如果修改，注意效果 */
  .comment-box {
    position: fixed;
    bottom: 5px;
    width: 200px;
    background-color: white;
  }
  /* 这里将评论框固定在屏幕下方；如果修改，注意效果 */
  /* 其他样式... */
}

</style>