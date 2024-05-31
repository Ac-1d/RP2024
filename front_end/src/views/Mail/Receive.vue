<template>
  <el-container style="margin-left: 5vw;">
    <el-table :data="rows" style="width: 100%;">
      <el-table-column label="写信人" prop="from" width="180"></el-table-column>
      <el-table-column prop="title" label="主题" width="180"></el-table-column>
      <el-table-column prop="date" label="时间">
      </el-table-column>
      <el-table-column fixed="right" width="120">
        <template slot-scope="scope">
          <el-button @click="linkto({title: rows[scope.$index].title, content: rows[scope.$index]})"
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
      rows: [
        {from: "李涵", title: "水费通知", date: "2024-05-16 12:00:00", content:"hahahahahaha"},
        {from: "张立", title: "商务往来", date: "2024-05-17 18:30:00", content:"hehehe"},
      ], // 邮件信息，用于调试
    }
  }
}
</script>