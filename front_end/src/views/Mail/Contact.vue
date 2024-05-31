<template>
  <el-table :data="contacts" style="width: 100%">
    <el-table-column label="联系人昵称" prop="name" width="180"></el-table-column>
    <el-table-column label="联系人账户" prop="userid" width="180"></el-table-column>
    <el-table-column fixed="right" width="120">
      <template slot-scope="scope">
        <el-button @click.native.prevent="sendto(scope.$index, contacts)"
          type="text" size="small">发送消息
        </el-button>
      </template>
    </el-table-column>

    <el-table-column fixed="right" width="120">
      <template slot-scope="scope">
        <el-button @click.native.prevent="deleteRow(scope.$index, contacts)"
          type="text" size="small">移除
        </el-button>
      </template>
    </el-table-column>
  </el-table>
</template>

<script>
export default{
  name: 'Contact',
  data() {
    return {
      contacts: [],
    }
  },
  methods:{
    sendto(index, contacts){
      console.log('sending to '+contacts[index].name);
    },
    deleteRow(index, contacts){
      contacts.splice(index, 1);
    }
  }
}
</script>