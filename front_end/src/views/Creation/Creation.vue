<template>
  <el-container>
    <el-tabs tab-position="left" style="width: max-content;">
      <el-tab-pane label="作品上传"><UploaderW/></el-tab-pane>
      <el-tab-pane label="内容管理"><Works/></el-tab-pane>
      <el-tab-pane label="评论数据"><Reviews/></el-tab-pane>
    </el-tabs>
  </el-container>
</template>

<script>

import Works from '@/views/Creation/Works.vue';
import Reviews from '@/views/Creation/Reviews.vue';
import UploaderW from '@/views/Creation/UploaderW.vue';

export default{
  name: 'Creation',
  components: {
    Works,
    Reviews,
    UploaderW,
  }
}

</script>