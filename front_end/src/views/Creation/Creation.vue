<template>
  <div class="center">
    <header class="header">
      <div class="header-content">
        <div class="avatar">
            <img :src="imgsrc" alt="Avatar" />
            <!-- {{ authorInfo.author_info }} -->
        </div>
        <ul class="info" v-if="authorInfo">
          <li class='NickName'><strong>昵称：</strong>{{ authorInfo.author_info.author_name }}</li>
          <li class='Level'><strong>知名度：</strong>{{ authorInfo.author_info.popularity }}分</li>
          <li class="Level"><el-rate :value="authorInfo.author_info.average_rating" diabled="true">作品评价</el-rate></li>
        </ul>
      </div>
    </header>
    <header class="down">
      <main class="main">
        <el-tabs type="border-card" tab-position="left" style="width: 88vw; height: 100vh;">
          <el-tab-pane aria-disabled="true">
            <span slot="label">作者信息
              <i class="el-icon-user"> </i>
            </span>
            <Reviews/>
          </el-tab-pane>

          <el-tab-pane>
            <span slot="label">内容管理
              <i class="el-icon-date"> </i> 
            </span>
            <Works/>
          </el-tab-pane>
          <el-tab-pane>
            <span slot="label">作品上传
              <i class="el-icon-upload2"> </i>
            </span>
            <Upload/>
          </el-tab-pane>
        </el-tabs>
      </main>
    </header>
  </div>
</template>

<script>

import Works from '@/views/Creation/Works.vue';
import Reviews from '@/views/Creation/Reviews.vue';
import Upload from '@/views/Creation/Upload.vue';
import {authorInfo} from '@/js/Api.js';

export default{
  name: 'Creation',
  data() {
    return {
      authorInfo: null,
      imgsrc: '',
    }
  },
  components: {
    Works,
    Reviews,
    Upload,
  },
  async created() {
    const user_id = this.$store.state.userInfo.id;
    const info = await authorInfo(user_id);

    this.authorInfo = info;
    console.log(this.authorInfo);

    let string = this.authorInfo.author_info.author_icon;  
    let delimiter = 'http://127.0.0.1:8000/';  
    let parts = string.split(delimiter);  
    this.imgsrc = 'user_' + parts[1];
    console.log(this.imgsrc);
  },
  methods: {
  }
}

</script>

<style scoped>
::v-deep .el-tabs__item {  
  display: inline-flex;
  text-align: left;
  font-size: large;
  width: 200px; 
  height: 40px;
}  
span {
  display: block; align-self: center; text-align: center;
}
.center {
  display: flex;
  flex-direction: column ;
  align-items: center;
  height: 100vh;
}

.header {

  background-image: url('../../assets/center_back.jpg');
  flex: 0 0 30%; /* 高度固定为30%，不可伸缩 */
  margin-top: 0.3%;
  margin-bottom: 0.3%;
  width: 90%;

  background-size: cover;
  background-position: top;

  color: #333; /* 设置字体颜色 */
  text-align: left;
  color: black;

  position: relative;
}
.down {
  flex: 1; /* 剩余空间均分给底部容器 */
  display: flex; /* 底部容器也需要是Flex布局来安排左右组件 */
  justify-content: space-between; /* 左右两侧分别靠边，中间自然间隔 */
  padding: 0 5%; /* 左右边界各留5%的间距 */
}


.avatar {
  position: absolute;
  left: 8%;
  top: 40%;
  width: 110px;
  height: 110px;
  border-radius: 50%;
  object-fit: cover;
  margin-bottom: 10px;
}

.avatar img {
  border-radius: 45%;
  width: 120px;
  height: 120px;
  object-fit: cover;
  border: 3px solid rgba(170, 110, 140, 0.3);

}
.NickName {
    font-size:30px;
}
.Level {
    font-size:20px;
}
.sidebar {
  flex: 0 0 18%;
  background-color: #f5f5f5;
  margin-right: 3%;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5); /* 增加阴影效果 */
  font-size: 14px; /* 设置字体大小 */
  color: #333; /* 设置字体颜色 */
  border-radius: 5px; /* 增加圆角 */
  font-family: 'Arial', sans-serif; /* 设置字体 */
  text-align: left; /* 左对齐文本 */
}
.infoSide{
  color: #555; /* 设置字体颜色 */
  list-style-type: none;
  margin-right: 10%;
  margin-left: 3%;
  text-align: left; /* 设置左对齐 */
  line-height: 30px; /* 设置行距为15px */
  padding:20px;
}
.main {
  flex:1;
  background-color: #fff;
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start; /* 左对齐 */
}

.info {
  position: relative; /* 文本相对于其正常流位置定位 */
  top:90%;

  margin-top: 10%;
  margin-left: 20%;
  list-style-type: none;
  color: #555; /* 设置字体颜色 */
  font-weight: bold;
}

strong{
color: #333; /* 设置加粗字体颜色 */
}
</style>