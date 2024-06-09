<template>
  <el-container>
    <el-tabs type="border-card" tab-position="left" style="width: 100vw; height: 100vh;">
      <el-tab-pane aria-disabled="true">
        <span slot="label">作者信息
          <i class="el-icon-user"> </i>
        </span>
        <Works/>
      </el-tab-pane>

      <el-tab-pane>
        <span slot="label">内容管理
          <i class="el-icon-date"> </i>
        </span>
        <Works/>
      </el-tab-pane>
      <el-tab-pane>
        <span slot="label">作品上传
          <i class="el-icon-upload2"> </i>
        </span>
        <Upload/>
      </el-tab-pane>
      <el-tab-pane>
        <span slot="label">评论数据
          <i class="el-icon-s-data"> </i>
        </span>
        <Reviews/>
      </el-tab-pane>
    </el-tabs>
  </el-container>
</template>

<script>

import Works from '@/views/Creation/Works.vue';
import Reviews from '@/views/Creation/Reviews.vue';
import Upload from '@/views/Creation/Upload.vue';
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
  },
  mounted() {
    console.log(this.$store.state.userInfo);
    if (!this.$store.state.userInfo['is_author']) {
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
    },
  }
}

</script>

<style scoped>
::v-deep .el-tabs__item {
  display: inline-flex;
  text-align: left;
  font-size: large;
  width: 200px;
  height: 40px;
}
span {
  display: block; align-self: center; text-align: center;
}
</style>