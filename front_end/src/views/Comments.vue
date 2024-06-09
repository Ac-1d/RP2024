<template>
  <el-container class="layout-round-middle">
    <!-- 评论显示 -->
    <el-main>
      <div v-for="(comment, index) in comments" :key="index">
        <!-- 环绕显示的每条评论 -->
        <div>
          <el-row style="border-top: 1px solid grey;">
              <el-link class="text-larger" style="float: left;" type="primary">{{ comment.username }}</el-link>
              <el-rate class="text-larger" style="float: left;" v-model="comment.up_number"
              disabled text-color="#ff9900"></el-rate>
              <el-link class="text-larger" style="float: left;" type="primary">{{ todate(comment.comment_time) }}</el-link>
          </el-row>
          <el-row><div class="auto-wrap">
            <p class="text-medium">{{ comment.comment_content }} </p>
          </div></el-row>
        </div>
      </div>
    </el-main>
    <!-- 评论、回复框 -->
    <el-footer style="min-height: 10vh;">
      <el-form :inline="true">
        <el-form-item style="width:60vw;">
          <textarea style="width: 60vw; border: 1px solid black;" v-model="newComment.content"></textarea>
        </el-form-item>
        <el-form-item style="width:10vw;">
          <el-rate v-model="newComment.up_number" :colors="colors"></el-rate>
          <el-button @click="addComment" style="float: left;">发送</el-button>
        </el-form-item>
      </el-form>
    </el-footer>
    <Login_window :dialogflag="logvisible" @closedia="closeDialog"></Login_window>
  </el-container>
</template>

<script>
import { addComments, getComments } from '@/js/Api.js';
import { extractDateTime } from '@/js/Time.js';
import Login_window from '@/components/Login_window.vue';

import '@/css/text.css';
import '@/css/layout.css';

export default {
  name: "Comments",
  components: { Login_window },
  data() {
    return {
<<<<<<< HEAD
      bookId: this.$store.getters.currentBookId, 
      
      chapterId: this.$store.getters.currentChapterId,
      
      userInfo: null,

      comments: null,// 已有评论

=======
      bookId: this.$route.params.bookId, // 从路由参数中获取 bookId
      chapterId: this.$store.getters.currentChapterId, // 从 Vuex 中获取当前章节ID
      userInfo: this.$store.state.userInfo, // 从 Vuex 中获取用户信息
      comments: [], // 已有评论
>>>>>>> zhengyujiejie
      newComment: {
        novel_id: null,
        chapter_id: null,
        user_id: this.userInfo ? this.userInfo.id : null,
        content: '',
        up_number: 0, // 评分，0表示未评分
      },
      // 评分显示颜色
      colors: ['#99A9BF', '#F7BA2A', '#FF9900'],
      // 显示登录界面
      logvisible: false,
    };
  },
<<<<<<< HEAD
  async created() {// 该页面创建的时候，就通过向后端发送请求，载入评论
    // this.bookId = this.$route.params.bookId;
    console.log(this.bookId + ' ' + this.chapterId);
    const respond = await getComments(this.bookId, this.chapterId);
    this.comments = respond;
    this.newComment.novel_id = this.bookId;
    this.newComment.chapter_id = this.chapterId;
    if(this.$store.state.loggedIn)
      this.userInfo = this.$store.state.userInfo; // 如果登录，载入当前用户信息
    // console.log(this.comments);
    console.log();
=======
  async created() {
    this.newComment.novel_id = this.bookId;
    this.newComment.chapter_id = this.chapterId;
    await this.fetchComments();
>>>>>>> zhengyujiejie
  },
  methods: {
    async fetchComments() {
      try {
        const response = await getComments(this.bookId, this.chapterId);
        this.comments = response;
      } catch (error) {
        console.error('Error fetching comments:', error);
      }
    },
    todate(time) {
      return extractDateTime(time);
    },
    showLogdialog() {
      this.logvisible = true;
    },
    closeDialog() {
      this.logvisible = false;
    },
    async addComment() {
      if (!this.userInfo) {
        this.showLogdialog();
        return;
      }
      if (this.newComment.content === '') {
        this.openMsg('请留下您的意见');
        return;
      }
      if (this.newComment.up_number === 0) {
        this.openMsg('请为此书评分');
        return;
      }
      try {
        await addComments(this.newComment);
        await this.fetchComments();
        this.newComment.content = '';
      } catch (error) {
        console.error('Error adding comment:', error);
      }
    },
    openMsg(msg) {
      this.$alert(msg, '提示', {
        confirmButtonText: '确定',
        callback: action => {
          this.$message({
            type: 'info',
            message: `action: ${ action }`
          });
        }
      });
    },
  }
};
</script>

<style scoped>
.book-detail {
  margin: 20px auto;
  max-width: 800px;
  text-align: left;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 5px;
  background-color: #f9f9f9;
}

.header {
  display: flex;
  justify-content: space-between;
}

.title-section {
  flex: 2;
}

.rating-section {
  flex: 1;
  text-align: center;
}

.book-info {
  display: flex;
  margin-bottom: 20px;
}

.book-cover {
  cursor: pointer;
  transition: transform 0.3s ease;
}

.book-cover:hover {
  transform: scale(1.1);
}

.book-info img {
  width: 150px;
  height: 200px;
  margin-right: 20px;
}

.details p {
  margin: 5px 0;
}

.read-button {
  display: block;
  margin-top: 10px;
  padding: 5px 10px;
  background-color: #007bff;
  border: none;
  color: white;
  cursor: pointer;
  border-radius: 5px;
}

.read-button:hover {
  background-color: #0056b3;
}

.rating {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.rating h2 {
  margin-bottom: 10px;
}

.score {
  font-size: 24px;
  font-weight: bold;
}

.rating-distribution {
  margin-top: 10px;
}

.rating-bar {
  display: flex;
  align-items: center;
  margin-bottom: 5px;
}

.rating-bar .bar {
  flex: 1;
  height: 10px;
  background: #eee;
  margin: 0 10px;
  position: relative;
}

.rating-bar .fill {
  height: 100%;
  background: orange;
}

.actions, .extra-actions {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.read-status {
  margin-right: 10px;
  padding: 5px 10px;
  background-color: #f0f0f0;
  border: 1px solid #ddd;
  border-radius: 5px;
}

.rating {
  display: flex;
  align-items: center;
}

.rating span {
  margin-right: 5px;
}

.stars {
  cursor: pointer;
}

.stars .active-star {
  color: orange;
}

.stars .inactive-star {
  color: #ccc;
}

.extra-actions a {
  margin-right: 10px;
  text-decoration: none;
  color: #007bff;
}

.extra-actions .icon {
  margin-right: 5px;
}

.extra-actions .recommend {
  padding: 5px 10px;
  background-color: #dff0d8;
  border: 1px solid #d6e9c6;
  border-radius: 5px;
  color: #3c763d;
}

.description, .author-info, .professional-reviews, .table-of-contents, .book-reviews, .book-chapters {
  margin-bottom: 20px;
}

.description h2, .author-info h2, .professional-reviews h2, .table-of-contents h2, .book-reviews h2, .book-chapters h2 {
  margin-bottom: 10px;
}

.table-of-contents ul, .book-chapters ul {
  list-style-type: disc;
  padding-left: 20px;
}

.comment {
  background: #f5f5f5;
  padding: 10px;
  border-radius: 5px;
  margin-bottom: 10px;
}
</style>
