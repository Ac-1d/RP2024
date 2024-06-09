<template>
<div>
  <el-table
    :data="TableData"
    stripe
    style="width: 100%">
    <el-table-column
      prop="chapter_info.novel_name"
      label="书名"
      width="180">
    </el-table-column>
    <el-table-column
      prop="chapter_info.novel_author"
      label="作者"
      width="180">
    </el-table-column>
    <el-table-column
      prop="chapter_info.category"
      label="分类">
    </el-table-column>
    <el-table-column
      prop="chapter_info.title"
      label="章节名">
    </el-table-column>


  </el-table>
</div>
</template>

<script>
import axios from 'axios';
  export default {
    name:'historyRecord',
    data() {
      return {
        TableData:[],
        tableData: [{
          date: '2016-05-02',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄'
        }, {
          date: '2016-05-04',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1517 弄'
        }, {
          date: '2016-05-01',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1519 弄'
        }, {
          date: '2016-05-03',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1516 弄'
        }]
      }
    },
    created(){
        console.log("我被创建了");
        this.getReadRecord();
    },
    methods: {
        getReadRecord: async function() {
            console.log("开始获取记录");
            try{
                const response = await axios.get('/novels/get_recently',{
                    params: {
                        user_id: this.$store.state.userInfo.id,
                     }

                });
                console.log("record:"+response);
                this.TableData = response.data.recent_reads;
            }catch(error){
                console.error(error);
            }

        },
    }
  }
</script>