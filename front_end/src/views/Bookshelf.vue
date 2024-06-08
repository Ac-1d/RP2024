<template>
  <el-container>
    <el-tabs type="border-card" tab-position="left" style="width: 100vw; height: 100vh;">
      <el-tab-pane>
        <span slot="label">按喜好排序
          <i class="el-icon-user"> </i>
        </span>
        <Shelf/>
      </el-tab-pane>

      <el-tab-pane>
        <span slot="label">按更新时间
          <i class="el-icon-date"> </i>
        </span>
        <Shelf/>
      </el-tab-pane>

      <el-tab-pane>
        <span slot="label">阅读历史记录
          <i class="el-icon-user"> </i>
        </span>
        <historyRecord/>
      </el-tab-pane>


    </el-tabs>
  </el-container>
</template>

<script>
import Shelf from '@/views/Shelf.vue';
import historyRecord from '@/views/historyRecord.vue';
export default {
  name: "Bookshelf",
  components: {
    Shelf,
    historyRecord,
  },
};
</script>

<style scoped>
/* 添加页面的样式 */
</style>
