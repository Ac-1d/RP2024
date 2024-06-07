<template>
  <el-container>
    <el-tabs type="border-card" tab-position="left" style="width: max-content;">
      <el-tab-pane><span slot="label">
        <i class="el-icon-date"></i> 内容管理</span>
        <!--  label="内容管理" -->
        <Works/>
      </el-tab-pane>
      <el-tab-pane><span slot="label">
        <i class="el-icon-upload2"> 作品上传</i>
      </span>
        <Upload/>
      </el-tab-pane>
      <el-tab-pane><span slot="label">
        <i class="el-icon-s-data"> 评论数据</i>
      </span>
        <Reviews/>
      </el-tab-pane>
    </el-tabs>
    <Login_window :dialogflag="logvisible" @closedia="closeDialog"></Login_window>
  </el-container>
</template>

<script>

import Works from '@/views/Creation/Works.vue';
import Reviews from '@/views/Creation/Reviews.vue';
import Upload from '@/views/Creation/Upload.vue';
import Login_window from '@/components/Login_window.vue';
import {beAuthor} from '@/js/Api.js';

export default{
  name: 'Creation',
  data() {
    return {
      logvisible: false,
      beAuthor: false,
      works: [],
      category: [],
    }
  },
  components: {
    Works,
    Reviews,
    Upload,
    Login_window,
  },
  mounted() {
    if (!this.$store.state.loggedIn) {
      this.showDialog('login');return;
    } else if (!this.$store.state.userInfo['is_author']) {
      console.log(this.$store.state.userInfo);
      this.becomeAuthor();return;
    }
  },
  methods: {
    becomeAuthor() {
      this.$alert('成为作者？', '提示', {
        confirmButtonText: '确定',
        callback: action => {
          this.$message({
            type: 'success',
            message: `be author: ${ action }, welcome`
          });
        beAuthor(this.$store.state.userInfo.id);
      }});
      // this.showDialog('login');
    },
    showDialog(option) {
      if (option == 'login') this.logvisible = true;
      else if (option == 'beAuthor') this.beAuthor = true;
    },
    closeDialog(option) {
      if (option == 'login') this.logvisible = false;
      else if (option == 'beAuthor') this.beAuthor = false;
      if(!this.$store.state.loggedIn) {// 如果没有登录成功
        this.$router.push({name: 'Home'});
        // this.$message({
        //   type: 'error',
        //   message: `登录失败`
        // });
      }
    },
  }
}

</script>