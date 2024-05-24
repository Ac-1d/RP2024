<template>
  <div class="side-nav">
    <div class="side-nav-item">
      <router-link to="/mail/send"
      style="color:white;text-decoration:none;">写信</router-link>
    </div>
    <div class="side-nav-item">
      <router-link to="/mail/recv"
      style="color:white;text-decoration:none;">收信</router-link>
    </div>
    <div class="side-nav-item">
      <router-link to="/mail/recv"
      style="color:white;text-decoration:none;">草稿箱</router-link>
    </div>
    <div class="side-nav-item">
      <router-link to="/mail/recv"
      style="color:white;text-decoration:none;">联系人</router-link>
    </div>
  </div>
</template>
<script>
export default{
  name:'Mail',
}
</script>
<style>
.side-nav {
  font-weight: bold;
  color:#EEEEEE;
  position: fixed;
  top: 50%;
  left: 0;
  transform: translateY(-50%);
  background: rgba(0, 0, 0, 0.7);
  border-radius: 0 10px 10px 0;
  padding: 10px;
  z-index: 1;
}
.side-nav-item {
  text-align: center;
  color: white;
  padding: 10px;
  margin: 5px 0px;
  cursor: pointer;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 5px;
}
.side-nav-item:hover {
  background: #007bff;
  color: white;
}
</style>