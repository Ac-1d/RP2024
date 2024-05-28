<template>
  <el-container>
    <el-tabs tab-position="top" type="card" style="width: 100%;">
      <el-tab-pane label="写信"><Send/></el-tab-pane>
      <el-tab-pane label="收信"><Receive/></el-tab-pane>
      <el-tab-pane label="草稿箱">草稿箱</el-tab-pane>
      <el-tab-pane label="联系人">联系人</el-tab-pane>
    </el-tabs>
  </el-container>
</template>

<script>
import Receive from '@/views/Mail/Receive.vue';
import Send from '@/views/Mail/Send.vue';

export default{
  name:'Mail',
  components: {
    Receive,
    Send,
  }
}
</script>