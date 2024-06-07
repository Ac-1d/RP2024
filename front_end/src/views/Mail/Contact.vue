<template>
  <el-container class="layout-middle">
      
    <el-main>
      <el-button type="text" style="float: left;" @click="dialogVisible = true">添加</el-button>

      <el-dialog
        title="添加联系人"
        :visible.sync="dialogVisible"
        width="30%">
        <el-form>
          <el-form-item label="联系人"><el-input v-model="newContact.name"></el-input></el-form-item>
          <el-form-item label="账户"><el-input v-model="newContact.userid"></el-input></el-form-item>
          <el-form-item><el-button @click="dialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="dialogVisible = false">确 定</el-button></el-form-item>
        </el-form>
      </el-dialog>

      <el-table :data="contacts" style="width: 100%">
        <el-table-column label="联系人" prop="name" width="180"></el-table-column>
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
    </el-main>
  </el-container>
</template>

<script>
import "@/css/layout.css";
export default{
  name: 'Contact',
  data() {
    return {
      dialogVisible: false, newContact: {name: '', userid: ''},
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
    },
    addContact(name, userid){
      this.contacts.push({name: name, userid: userid});
      // axios 请求
    }
  }
}
</script>