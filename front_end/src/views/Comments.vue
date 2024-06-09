<template>
  <el-container class="layout-round-middle">
    <!-- 评论显示 -->
    <el-main>
      <div v-for="(comment, index) in comments" :key="index">
        <!-- 循环显示的每条评论 -->
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
import {addComments} from '@/js/Api.js';
import {getComments} from '@/js/Api.js';
import {extractDateTime} from '@/js/Time.js';
import Login_window from '@/components/Login_window.vue';

import '@/css/text.css';
import '@/css/layout.css';

export default {
  name: "Comments",
  components: { Login_window },
  data() {
    return {
      bookId: 2, chapterId: 2,
      
      userInfo: null,

      comments: null,// 已有评论

      newComment: {
        novel_id: null, 
        chapter_id: null, 
        // user_id: this.userInfo.id,
        user_id: 3,

        content: '',
        up_number: 0,// 评级，代表用户支持度，0代表尚未评分
      },

      // 评级显示颜色
      colors: ['#99A9BF', '#F7BA2A', '#FF9900'],

      // 显示登录界面
      logvisible: false,
    };
  },
  async created() {// 该页面创建的时候，就通过向后端发送请求，载入评论
    // this.bookId = this.$route.params.bookId;
    const respond = await getComments(this.bookId, this.chapterId);
    this.comments = respond;
    this.newComment.novel_id = this.bookId;
    this.newComment.chapter_id = this.chapterId;
    if(this.$store.state.loggedIn)
      this.userInfo = this.$store.state.userInfo; // 如果登录，载入当前用户信息
    // console.log(this.comments);
  },
  methods: {
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
      let newComment = this.newComment;
      if (this.userInfo == null) {
        this.showLogdialog();return;
      }
      if (newComment.content == '') {
        this.openMsg('请留下宝贵意见');return;
      }
      if (newComment.up_number == 0) {
        this.openMsg('请您打分');return;
      }
      await addComments(newComment);
      await getComments(this.bookId, this.chapterId);
      this.content = '';
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