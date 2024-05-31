<template>
  <el-container class="layout-round-middle">
    <!-- 用户信息 -->
    <el-header style="position: left">
      <el-button class="text-larger" style="float: left;" type="primary"
      icon="el-icon-caret-left" @click="goback()"></el-button>
      <p>用户名：{{ myname }}</p>
      <p>ID-{{ myid }}</p>
    </el-header>
    <!-- 评论显示 -->
    <el-main>
      <div v-for="(comment, index) in paginatedComments" :key="index">
        <!-- 循环显示的每条评论 -->
        <div>
          <el-row style="border-top: 1px solid grey;">
            <el-col :span="20" >
              <el-link class="text-larger" style="float: left;" type="primary">{{ comment.author }}</el-link>
              <el-rate class="text-larger" style="float: left;" v-model="comment.rank_value" 
              disabled text-color="#ff9900"></el-rate>
              <el-link class="text-larger" style="float: left;" type="primary">{{ comment.time }}</el-link>
            </el-col>
            <el-col :span="16">
              <div class="auto-wrap">
                <p class="text-medium">{{ comment.text }} </p>
              </div>
            </el-col>
            <el-col :span="16">
              <el-button class="text-larger" style="float: left;" type="text" 
              icon="el-icon-caret-top" @click="likeComment(index)">{{ comment.likes > 0 ? comment.likes:'' }}</el-button>
              <el-button class="text-larger" style="float: left;" type="text" 
              icon="el-icon-edit" @click="beginReply(index)">回复{{ comment.replies.length }}</el-button>
              <el-button class="text-larger" style="float: left;" type="text" 
              :icon="comment.showReply ? 'el-icon-arrow-up':'el-icon-arrow-down' " @click="showReply(index)"></el-button>
              <!-- element的type如果为text，则结果是文字按钮 -->
            </el-col>
            <!-- 回复区 -->
            <el-col v-if="comment.showReply">  
              <!-- 回复显示 -->
              <div style="margin-left: 100px" v-for="(reply, replyIndex) in comment.replies" 
              :key="replyIndex" class="auto-wrap">  
                <div>
                  <el-link class="text-larger">{{ reply.author }}</el-link>
                </div>
                <p class="text-medium">{{ reply.text }}</p>  
              </div>  
            </el-col>
          </el-row>
        </div>
      </div>
      <!-- 翻页栏 -->
      <div class="pagination">
        <button @click="prevPage" :disabled="currentPage === 1">&lt;</button>
        <span v-for="page in totalPages" :key="page" 
        :class="['page-dot', { active: page === currentPage }]" @click="goToPage(page)"></span>
        <button @click="nextPage" :disabled="currentPage === totalPages">&gt;</button>
      </div>
    </el-main>
    <!-- 评论、回复框 -->
    <el-main>
      <el-form :inline="true">
        <el-form-item style="width: 20vw;">
          <div><el-rate v-model="value" :colors="colors"></el-rate>
          <el-button v-if="replying" @click="endReply" style="float: left;">返回评论</el-button><!-- 退出回复，返回评论 -->
          <el-button @click="addComment" style="float: left;">发送</el-button></div>
        </el-form-item>
        <el-form-item>
          <el-input :placeholder="replying?('正在回复'+comments[replyIndex].author):('输入评论')"
          type="textarea" v-model="content" maxlength="10000" show-word-limit style="width: 50vw; display: flex;"/>
        </el-form-item>
      </el-form>
    </el-main>
  </el-container>
</template>

<script>
import {currentTime} from "../js/Time.js";
import bookComments from '@/assets/comments.json';
import '@/css/text.css';
import '@/css/layout.css';
export default {
  name: "CommentBlock",
  components: {
  },
  props: {
    myname: {
      type: String,
      default: '匿名'
    },// 传入用户名
    myid: {
      type: Number,
      default: 100
      // 传入用户id
    }
  },
  data() {
    return {
      bookId: 1,
      currentPage: 1, // 当前是第几页
      commentsPerPage: 5,
      value: 0, // 当前用户选择的评分
      comments: bookComments,// 已有评论
      content: '',// 输入内容
      replying: false,// 正在回复
      replyIndex: 0,// 回复的评论号
      colors: ['#99A9BF', '#F7BA2A', '#FF9900'],
    };
  },
  created() {
    const bookId = this.$route.params.bookId;
    this.bookId = bookId;
    // console.log('id is : '+bookId);
    this.comments = this.getCommentsByBookId(bookId);
  },
  methods: {
    prevPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
      }
    },
    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++;
      }
    },
    goToPage(page) {
      this.currentPage = page;
    },
    goback() {
      this.$router.push({ name: 'BookDetail', params: {bookId: this.bookId}  });
    },
    getCommentsByBookId(id) {
      const commentsData = require("@/assets/comments.json");
      return commentsData.find(comment => comment.id == id).comments;
    },
    addComment() {
      if (this.content) {
        if (this.replying) {
          const newReply = {
            text: this.content, 
            author: this.myname
          };
          this.comments[this.replyIndex].replies.push(newReply);
          this.endReply();
        }
        else {
          const newComment = { 
            rank_value: this.value,
            text: this.content, 
            author: this.myname, 
            showReply: false,
            likes: 0, 
            replyText: '',
            replies: [],
            time: currentTime()
          };
          this.comments.push(newComment);
        }
        this.content = '';
      }
    },
    likeComment(index) {
      if (index < this.comments.length && index >= 0) {
        this.comments[index].likes++;
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
  },
  computed: {
    totalPages() {
      return Math.ceil(this.comments.length / this.commentsPerPage);
    },
    paginatedComments() {
      const start = (this.currentPage - 1) * this.commentsPerPage;
      const end = start + this.commentsPerPage;
      return this.comments.slice(start, end);
    }
  }
};  
</script>

<style>
/* 翻页栏样式 */
.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
  position: fixed; /* 固定位置 */
  bottom: 20px; /* 距离底部 */
  left: 50%; /* 水平居中 */
  transform: translateX(-50%);
  background: white;
  padding: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  border-radius: 5px;
}

.pagination button {
  background: none;
  border: none;
  font-size: 20px;
  cursor: pointer;
}

.pagination .page-dot {
  width: 10px;
  height: 10px;
  background-color: lightgray;
  border-radius: 50%;
  margin: 0 5px;
  cursor: pointer;
}

.pagination .page-dot.active {
  background-color: gray;
}
</style>
