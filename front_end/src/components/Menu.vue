<template>
<div>
<el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
  <el-menu-item index="1">登录</el-menu-item>
  <el-menu-item index="4">注册</el-menu-item>
</el-menu>
</div>
</template>

<script>
  export default {
  name: "Menu",
  props: {
    Num: Number,

  },
  data() {
    return {
      activeIndex: '1',
    };
  },
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      }
    }
  }
</script>