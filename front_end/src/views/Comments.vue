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
        <el-form-item>
          <textarea v-model="newComment.content"></textarea>
        </el-form-item>
        <el-form-item>
          <el-rate v-model="newComment.up_number" :colors="colors"></el-rate>
          <el-button @click="addComment" style="float: left;">发送</el-button>
        </el-form-item>
      </el-form>
    </el-footer>
  </el-container>
</template>

<script>
import {addComments} from '@/js/Api.js';
import {getComments} from '@/js/Api.js';
import {extractDateTime} from '@/js/Time.js';

import '@/css/text.css';
import '@/css/layout.css';
export default {
  name: "Comments",

  data() {
    return {
      bookId: 2, chapterId: 1,
      // userInfo: this.$store.state.userInfo, // 当前用户信息
      userInfo: null,

      // 评论分页功能
      currentPage: 1, // 当前是第几页
      commentsPerPage: 5, // 每页有五条评论

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
    };
  },
  async created() {// 该页面创建的时候，就通过向后端发送请求，载入评论
    // this.bookId = this.$route.params.bookId;
    this.comments = await getComments(this.bookId, this.chapterId);
    this.newComment.novel_id = this.bookId;
    this.newComment.chapter_id = this.chapterId;
    console.log(this.comments);
  },
  methods: {
    todate(time) {
      return extractDateTime(time);
    },
    async addComment() {
      let newComment = this.newComment;
      if (newComment.content == '') {
        return;
      }
      if (newComment.up_number == 0) {
        return;
      }
      await addComments(newComment);
      // this.comments.push(this.newComment);
      // this.content = '';
    }
  }
};  
</script>