<template>
  <div class="profile">
    <div class="avatar">
      <img src="@/assets/Avatar.jpg" alt="Avatar" width="200" height="150" />
    </div>
    <div class="info">
      <h2>昵称：{{ nickname }}</h2>
      <h2>等级：{{ level }}</h2>
      <h2>个人签名：{{ signature }}</h2>
    </div>
  <button @click="showLoginModal = true">登录|注册</button>
  <LoginModal v-if="showLoginModal" @close="showLoginModal = false" />

  </div>
</template>

<script>
import LoginModal from '@/views/log.vue';
export default {
   components: {
      LoginModal
   },
  data() {
    return {
      nickname: "John Doe",
      signature: "好好学习，天天向上!",
      level:"lv7",
      avatarUrl: "https://example.com/avatar.jpg", // 你的头像图片地址
      showLoginModal: false
    };
  }
};



</script>

<style>
.profile {
  display: flex;
  align-items: center;
}

.avatar {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  overflow: hidden;
  margin-right: 20px;
}

.avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.info {
  font-size: 24px;
}
</style>
