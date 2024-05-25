<!-- LoginModal.vue -->
<template>
  <div v-if="showModal" class="modal">
    <div class="modal-content">
      <h2>Login</h2>
      <form @submit.prevent="handleLogin">
        <input type="text" placeholder="Username" v-model="username" required />
        <input type="password" placeholder="Password" v-model="password" required />
        <button type="submit">Login</button>
      </form>
      <button @click="closeModal">Close</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showModal: false,
      username: '',
      password: ''
    };
  },
  methods: {
    closeModal() {
      this.showModal = false;
      // 可以在这里添加清除输入框的逻辑
    },
    handleLogin() {
      // 这里添加登录逻辑，如验证用户名和密码，调用API等
      console.log('Trying to login with:', this.username, this.password);
      // 登录成功后关闭模态框
      this.closeModal();
    }
  }
};
</script>

<style scoped>
.modal {
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(0,0,0,0.4);
}

.modal-content {
  background-color: #fefefe;
  margin: 15% auto;
  padding: 20px;
  border: 1px solid #888;
  width: 30%;
}
</style>