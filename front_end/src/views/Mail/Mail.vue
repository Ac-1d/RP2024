<template>
  <el-container class="layout-middle">
    <el-tabs type="card" closable @tab-remove="removeTab" v-model="page"
    style="width: 100%; background-color: aliceblue;">
      <el-tab-pane label="写信" name="send" :closable="false"><Send @draft="storeDraft"/></el-tab-pane>
      <el-tab-pane label="收信" name="receive" :closable="false"><Receive @custom-event="addTab"/></el-tab-pane>
      <el-tab-pane label="草稿箱" name="draft" :closable="false"><Drafts ref="DraftsRef"/></el-tab-pane>
      <el-tab-pane label="联系人" name="contact" :closable="false"><Contact @send="addTab"/></el-tab-pane>
      <el-tab-pane
        v-for="item in editableTabs"
        :key="item.name"
        :label="item.title"
        :name="item.name" lazy>
        <Send v-if="item.type=='Send'" :Info="item.content" @draft="storeDraft"/>
        <MailDetail v-if="item.type=='MailDetail'" :mailItem="item.content"/>
      </el-tab-pane>
    </el-tabs>
    <!-- <ParentComponent/> -->
  </el-container>
</template>

<script>
import Receive from '@/views/Mail/Receive.vue';
import Send from '@/views/Mail/Send.vue';
import Drafts from '@/views/Mail/Drafts.vue';
import Contact from '@/views/Mail/Contact.vue';
import MailDetail from '@/views/Mail/MailDetail'
// import ParentComponent from '@/views/Mail/ParentComponent.vue';

export default{
  name:'Mail',
  components: {
    Receive,
    Send,
    Drafts,
    Contact,
    MailDetail,
    // ParentComponent,
  },
  data() {
    return {
      page:'receive',
      tabid: 0,
      editableTabs: [],
    }
  },
  methods: {
    addTab(data) {
      // console.log('adding...');
      let tabname = data.title;
      let tablabel = data.title;
      let tabcontent = data.content;

      let NewTabName = tabname + '-' + this.tabid++;// 防止重名；不过这里tablabel是可以重名的

      let item = {name: NewTabName, title: tablabel, content:tabcontent, type: data.type};
      this.editableTabs.push(item);
      this.page = NewTabName;
    },
    removeTab(targetName) {
      let tabs = this.editableTabs;
      let activeName = this.page;
      if (activeName === targetName) {
        tabs.forEach((tab, index) => {
          if (tab.name === targetName) {
            let nextTab = tabs[index + 1] || tabs[index - 1];
            if (nextTab) {
              activeName = nextTab.name;
            }
          }
        });
      }
      
      this.page = activeName;
      this.editableTabs = tabs.filter(tab => tab.name !== targetName);
      if (this.editableTabs.length == 0) {
        this.page="contact";
      }
    },
    storeDraft(draft) {
      // console.log(draft);
      this.$refs.DraftsRef.addRow(draft);
      this.$alert('添加草稿 收信人：'+draft.sendto, '提示', {
        confirmButtonText: '确定',
        // callback: action => {
        //   this.$message({
        //     type: 'info',
        //     message: `action: ${ action }`
        //   });
        // }
      });
    },
  }
}
</script>