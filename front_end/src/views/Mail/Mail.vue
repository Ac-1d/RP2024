<template>
  <el-container>
    <el-tabs type="card" closable @tab-remove="removeTab" v-model="page"
    style="width: 100%; background-color: aliceblue;">
      <el-tab-pane label="写信" name="send"><Send/></el-tab-pane>
      <el-tab-pane label="收信" name="recieve" @custom-event="addTab"><Receive/></el-tab-pane>
      <el-tab-pane label="草稿箱" name="draft"><Drafts/></el-tab-pane>
      <el-tab-pane label="联系人" name="contact"><Contact/></el-tab-pane>
      <el-tab-pane
        v-for="item in editableTabs"
        :key="item.name"
        :label="item.title"
        :name="item.name" lazy>
        {{item.content}}
      </el-tab-pane>
    </el-tabs>
    <el-button @click="addTab({title: 1, content: 'hello from Mail'})">
      点击添加
    </el-button>
    <ParentComponent/>
  </el-container>
</template>

<script>
import Receive from '@/views/Mail/Receive.vue';
import Send from '@/views/Mail/Send.vue';
import Drafts from '@/views/Mail/Drafts.vue';
import Contact from '@/views/Mail/Contact.vue';
import ParentComponent from '@/views/Mail/ParentComponent.vue';

export default{
  name:'Mail',
  components: {
    Receive,
    Send,
    Drafts,
    Contact,
    ParentComponent,
  },
  data() {
    return {
      page:'send',
      tabid: 0,
      editableTabs: [],
    }
  },
  methods: {
    addTab(data) {
      console.log('adding...');
      let tabname = data.title;
      let tablabel = data.content;
      let NewTabName = tabname + '-' + this.tabid++;
      let item = {name: NewTabName, title: tablabel, content:''};
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
    }
  }
}
</script>