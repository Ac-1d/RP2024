<template>
  <el-container>
    
    <el-table :data="rows" style="width: 100%;">
      <el-table-column label="写信人" prop="from" width="180"></el-table-column>
      <el-table-column prop="title" label="主题" width="180"></el-table-column>
      <el-table-column prop="date" label="时间">
      </el-table-column>
      <el-table-column fixed="right" width="120">
        <template slot-scope="scope">
          <el-button @click="linkto({title: scope.$index, content: mails[scope.$index]})"
            type="text">查看
          </el-button>
        </template>
      </el-table-column>

      <el-table-column fixed="right" width="120">
        <template slot-scope="scope">
          <el-button @click.native.prevent="deleteRow(scope.$index, rows)"
            type="text">移除
          </el-button>
        </template>
      </el-table-column>
    </el-table>
    <div class="auto-wrap">
      <p class="text-medium">{{ current }} </p>
    </div>
    <button @click="$emit('custom-event', {title: 1, content: mails[1]})"></button>
  </el-container>
</template>
<script>
import '@/css/text.css';
export default{
  name: 'Receive',
  methods: {
    deleteRow(index, rows) {
      rows.splice(index, 1);
    },
    linkto(data) {
      console.log(data);
      this.$emit('custom-event', data); 
    }
  },
  data(){
    return {
      current: '', // 当前要显示的邮件内容
      rows: [
        {from: "李涵", title: "水费通知",   date: "2024-05-16 12:00:00"},
        {from: "张立", title: "商务往来",   date: "2024-05-17 18:30:00"},
      ], // 邮件信息，用于调试
      mails: [
        "hahahahahaha","hehehe",
      ], // 邮件内容，用于调试
    }
  }
}
</script>