<template>
  <div>
    <h1>搜索结果 "{{ $route.query.q }}"</h1>
    <div v-if="results.length">
      <div v-for="book in results" :key="book.id" class="search-result">
        <img :src="require(`@/assets/${book.image}`)" :alt="book.title" />
        <div>
          <h3>{{ book.title }}</h3>
          <p>{{ book.author }}</p>
          <p>{{ book.publisher }}</p>
          <p>{{ book.publish_date }}</p>
          <p>{{ book.price }}</p>
        </div>
      </div>
    </div>
    <div v-else>
      <p>未找到结果</p>
    </div>
  </div>
</template>

<script>
import booksData from "@/assets/book.json";
import booksData2 from "@/assets/bookSelf.json";

export default {
  data() {
    return {
      results: [],
      currentBooksData: booksData, // 默认数据集
    };
  },
  watch: {
    '$route': 'handleRouteChange', // 监听路由变化
  },
  methods: {
    handleRouteChange(to) {
      const createParam = parseInt(to.query.c, 10);
      this.currentBooksData = createParam === 0 ? booksData2 : booksData; // 根据create参数切换数据集
      if (to.query.q) {
        this.handleSearch(to.query.q);
      } else {
        this.results = []; // 如果没有查询参数，清空搜索结果
      }
    },
    handleSearch(query) {
      this.results = this.currentBooksData.filter(book =>
        book.title.includes(query) ||
        book.author.includes(query) ||
        book.isbn.includes(query)
      );
    },
  },
  mounted() {
    this.handleRouteChange(this.$route); // 页面初次加载时处理路由参数
  },
};
</script>

<style scoped>
.search-result {
  display: flex;
  margin-bottom: 20px;
}
.search-result img {
  width: 100px;
  height: 150px;
  margin-right: 20px;
}
.search-result h3 {
  margin: 0;
}
</style>

