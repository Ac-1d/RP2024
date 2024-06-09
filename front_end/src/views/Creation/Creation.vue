<template>
  <el-container>
    <el-tabs type="border-card" tab-position="left" style="width: 100vw; height: 100vh;">
      <el-tab-pane aria-disabled="true">
        <span slot="label">作者信息
          <i class="el-icon-user"> </i>
        </span>
        <Reviews/>
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
    </el-tabs>
  </el-container>
</template>

<script>

import Works from '@/views/Creation/Works.vue';
import Reviews from '@/views/Creation/Reviews.vue';
import Upload from '@/views/Creation/Upload.vue';
import {authorInfo} from '@/js/Api.js';
// import {beAuthor} from '@/js/Api.js';

export default{
  name: 'Creation',
  data() {
    return {
      logvisible: false,
      authorInfo: null,
    }
  },
  components: {
    Works,
    Reviews,
    Upload,
  },
  async created() {
    const user_id = this.$store.state.userInfo.id;
    this.authorInfo = await authorInfo(user_id);
  },
  methods: {
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