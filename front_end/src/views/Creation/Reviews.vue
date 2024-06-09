<template>
  <div class="home">

    <div class="content">

      <div class="main-content">
        <div class="category-bar">
          <span class="title">作者信息</span>
        </div><div class="separator"></div>

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
    }
  },
  async created() {
    const user_id = this.$store.state.userInfo.id;
    this.authorInfo = await authorInfo(user_id);
  },
}
</script>