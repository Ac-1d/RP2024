<template>
  <el-container>
    <el-tabs type="border-card" tab-position="left" style="width: 100vw; height: 100vh;">
      <el-tab-pane >
        <span slot="label" @click="Set0()">按喜好排序
          <i class="el-icon-user"> </i>
        </span>
        <Shelf :mode="choose"/>
      </el-tab-pane>

      <el-tab-pane >
        <span slot="label" @click="Set1()">按更新时间
          <i class="el-icon-date"> </i>
        </span>
        <Shelf :mode="choose"/>
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
  data(){
    return{
        choose: 0,
    };
  },
  methods: {
    Set0(){
        this.choose = 0;
        console.log("choose="+this.choose);
    },
    Set1(){
        this.choose = 1;
        console.log("choose="+this.choose);
    },
  }
};
</script>

<style scoped>
/* 添加页面的样式 */
</style>
