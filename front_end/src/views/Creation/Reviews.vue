<template>
  <div class="home">

    <div class="content">

      <div class="main-content">
        <div class="category-bar">
          <span class="title">作者信息</span>
        </div><div class="separator"></div>

        <div class="avatar" v-if="authorInfo"><img :src="imgsrc" alt="Avatar" /></div>

        <div class="info">
          <!-- {{ authorInfo }} -->
          <ul class='infoSide' v-if="authorInfo">
            <li><h1>资料卡片:</h1></li>
            <li>作者昵称：{{ authorInfo.author_info.author_name }}</li>
            <li>性别：{{ authorInfo.author_info.author_gender }}</li>
            <li>简介：{{ authorInfo.author_info.detail }}</li>
            <li>知名度：{{ authorInfo.author_info.popularity }}</li>
            <li>作品评级：<el-rate :value="authorInfo.author_info.average_rating" :disabled="true"></el-rate></li>
          </ul>
        </div>

      </div>
    </div>
  </div>
</template>


<script>
import "@/css/layout.css";
import {authorInfo} from '@/js/Api.js';

export default{
  name: 'Reviews',
  data() {
    return {
      authorInfo: null,
      imgsrc: '',
    }
  },
  computed: {},
  async created() {
    const user_id = this.$store.state.userInfo.id;
    const info = await authorInfo(user_id);
    this.authorInfo = info;

    // let string = this.authorInfo.author_info.author_icon;
    // let delimiter = 'http://127.0.0.1:8000/';  
    // let parts = string.split(delimiter);  
    // this.imgsrc = 'user_' + parts[1];
    this.imgsrc = require('@/assets/Avatar.jpg')
    // console.log(this.imgsrc);
    // console.log('authorInfo:');
    // console.log(this.authorInfo);
  },
}
</script>
<style scoped>
.infoSide{
  color: #555; /* 设置字体颜色 */
  margin-right: 10%;
  margin-left: 3%;
  text-align: left; /* 设置左对齐 */
  line-height: 30px; /* 设置行距为15px */
  padding:20px;
}
.info {
  /* position: relative; /* 文本相对于其正常流位置定位 */
  top:90%;

  margin-top: 10%;
  margin-left: 20%;
  color: #555; /* 设置字体颜色 */
  font-weight: bold; 
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
</style>
