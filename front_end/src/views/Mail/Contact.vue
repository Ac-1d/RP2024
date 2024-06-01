<template>
  <el-container class="layout-middle">
    <el-table :data="contacts" style="width: 100%">
      <el-table-column label="联系人昵称" prop="name" width="180"></el-table-column>
      <el-table-column label="联系人账户" prop="userid" width="180"></el-table-column>
      <el-table-column fixed="right" width="120">
        <template slot-scope="scope">
          <el-button @click.native.prevent="sendto(scope.$index, contacts)" type="text">发送消息
          </el-button>
        </template>
      </el-table-column>

      <el-table-column fixed="right" width="120">
        <template slot-scope="scope">
          <el-button @click.native.prevent="deleteRow(scope.$index, contacts)" type="text">移除
          </el-button>
        </template>
      </el-table-column>
    </el-table>
  </el-container>
</template>

<script>
import "@/css/layout.css";
export default{
  name: 'Contact',
  data() {
    return {
      contacts: [{name:'lzy', userid:101}, {name:'aaa', userid:102}],
    }
  },
  methods:{
    sendto(index, contacts){
      console.log('sending to '+contacts[index].name);
      let data = {
        title: '发送给'+contacts[index].name, 
        content: contacts[index].userid, 
        type: 'Send'};
      this.$emit('send', data); 
    },
    deleteRow(index, contacts){
      contacts.splice(index, 1);
    }
  }
}
</script>