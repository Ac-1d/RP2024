<template>
  <div>
    <Mail/>
    <el-container>
      <el-header>收信箱</el-header>
    </el-container>
    <el-container>
      <el-aside width="200px">侧边栏</el-aside>
      <el-main>信件</el-main>
      <el-container>
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
          <el-table-column
            fixed="right"
            label="操作"
            width="120">
            <template slot-scope="scope">
              <el-button
                @click.native.prevent="linkto(scope.$index, mails)"
                type="text"
                size="small">
                查看
              </el-button>
            </template>
          </el-table-column>

          <el-table-column
            fixed="right"
            label="操作"
            width="120">
            <template slot-scope="scope">
              <el-button
                @click.native.prevent="deleteRow(scope.$index, rows)"
                type="text"
                size="small">
                移除
              </el-button>
            </template>
          </el-table-column>
        </el-table>
        <div class="auto-wrap">
          <p class="text-medium">{{ current }} </p>
        </div>
      </el-container>
    </el-container>
  </div>
</template>
<script>
import Mail from '@/views/Mail/Mail.vue';
import '@/css/text.css';
export default{
  name: 'Receive',
  components: {
    Mail
  },
  methods: {
    deleteRow(index, rows) {
      rows.splice(index, 1);
    },
    linkto(index, mail) {
      this.current = mail[index];
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