<template>
  <div class="side-bar">
    <button @click="handleButtonClick('按钮1')">按钮1</button>
    <button @click="handleButtonClick('按钮2')">按钮2</button>
    <button @click="handleButtonClick('按钮3')">按钮3</button>
  </div>
</template>

<script>
export default {
  name: "SideBar",
  methods: {
    handleButtonClick(buttonName) {
      console.log(buttonName + ' clicked');
      // 在这里处理按钮点击事件
    }
  }
};
</script>

<style scoped>
.side-bar {
  display: flex;
  flex-direction: column;
  padding: 10px;
  background-color: #f8f8f8;
  border-right: 1px solid #ddd;
}
.side-bar button {
  padding: 10px;
  margin-bottom: 10px;
  background-color: #ddd;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
.side-bar button:hover {
  background-color: #ccc;
}
</style>
