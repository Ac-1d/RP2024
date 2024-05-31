<template>
  <el-container>
    <el-tabs tab-position="top" type="card" v-model="page"
    style="width: 100%; background-color: aliceblue;">
      <el-tab-pane label="写信" name="send"><Send/></el-tab-pane>
      <el-tab-pane label="收信" name="recieve"><Receive/></el-tab-pane>
      <el-tab-pane label="草稿箱" name="draft"><Drafts/></el-tab-pane>
      <el-tab-pane label="联系人" name="contact"><Contact/></el-tab-pane>
    </el-tabs>
  </el-container>
</template>

<script>
import Receive from '@/views/Mail/Receive.vue';
import Send from '@/views/Mail/Send.vue';
import Drafts from '@/views/Mail/Drafts.vue';
import Contact from '@/views/Mail/Contact.vue';

export default{
  name:'Mail',
  components: {
    Receive,
    Send,
    Drafts,
    Contact,
  },
  data() {
    return {
      page:'send',
    }
  }
}
</script>