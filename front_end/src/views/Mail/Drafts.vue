<template>
  <el-container class="layout-middle">
    <el-table :data="drafts" style="width: 100%;">
      <el-table-column label="收信人" prop="sendto" width="180"></el-table-column>
      <el-table-column label="时间" prop="time" width="180"></el-table-column>
      <el-table-column fixed="right" width="120">
        <template slot-scope="scope">
          <el-button @click.native.prevent="linkto(scope.$index, drafts)" type="text">查看
          </el-button>
        </template>
      </el-table-column>

      <el-table-column fixed="right" width="120">
        <template slot-scope="scope">
          <el-button @click.native.prevent="deleteRow(scope.$index, drafts)" type="text">移除
          </el-button>
        </template>
      </el-table-column>
    </el-table>
  </el-container>
  
</template>
<script>
export default{
  name: 'Drafts',
  data() {
    return {
      drafts: [], // 草稿列表
    }
  },
  methods: {
    deleteRow(index, rows) {
      rows.splice(index, 1);
    },
    linkto(index, mail) {
      this.current = mail[index];
    },
    addRow(draft) {
      this.drafts.push(draft); 
    },
  }
}
</script>