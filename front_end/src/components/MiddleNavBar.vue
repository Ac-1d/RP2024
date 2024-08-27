<template>
  <div class="middle-nav-bar">
    <div class="logo">RP</div>
    <input v-model="query" @keyup.enter="search" type="text" placeholder="书名、作者、ISBN" />
    <button @click="search">🔍</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      query: ""
    };
  },
  methods: {
    search() {
      if (this.query.trim()) {
        this.$router.push({ name: 'Search', query: { q: this.query ,c: 2} });
      }
    }
  }
};
</script>

<style scoped>
.middle-nav-bar {
  display: flex;
  align-items: center;
  padding: 10px 20px;
  background-color: #f8f8f8;
  border-bottom: 1px solid #ddd;
}
.logo {
  font-size: 24px;
  font-weight: bold;
  margin-right: 20px;
}
input[type="text"] {
  flex-grow: 1;
  padding: 5px;
  margin-right: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
}
button {
  padding: 5px 10px;
  background-color: #ddd;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
button:hover {
  background-color: #ccc;
}
</style>
