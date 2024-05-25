<template>
  <div>
    <Mail/>
    <h1>收信箱</h1>
    <div>
      <el-table
        :data="rows"
        style="width: 100%">
        <el-table-column
          label="写信人"
          prop="from"
          width="180">
        </el-table-column>
        <el-table-column
          prop="title"
          label="主题"
          width="180">
        </el-table-column>
        <el-table-column
          prop="date"
          label="时间">
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>
<script>
import Mail from '@/views/Mail/Mail.vue';
export default{
  name: 'Receive',
  components: {
    Mail
  },
  data(){
    return {
      rows: [
        {from: "李涵", title: "水费通知",   date: "2024-05-16 12:00:00"},
        {from: "张立", title: "商务往来",   date: "2024-05-17 18:30:00"},
      ], 
    }
  }
}
</script>
