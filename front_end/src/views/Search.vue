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

export default {
  data() {
    return {
      results: []
    };
  },
  watch: {
    '$route.query.q': {
      immediate: true,
      handler(query) {
        this.results = booksData.filter(book =>
          book.title.includes(query) ||
          book.author.includes(query) ||
          book.isbn.includes(query)
        );
      }
    }
  }
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
