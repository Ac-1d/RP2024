<template>
  <div class="book-detail">
    <h1>{{ book.title }}</h1>
    <div class="book-info">
      <img :src="bookImage" :alt="book.title" />
      <div class="details">
        <p><strong>作者:</strong> {{ book.author }}</p>
        <p><strong>出版社:</strong> {{ book.publisher }}</p>
        <p><strong>出版时间:</strong> {{ book.publish_date }}</p>
        <p><strong>页数:</strong> {{ book.pages }}</p>
        <p><strong>价格:</strong> {{ book.price }}</p>
        <p><strong>ISBN:</strong> {{ book.isbn }}</p>
      </div>
    </div>
    <div class="rating">
      <h2>豆瓣评分</h2>
      <p class="score">{{ book.rating }} <span>({{ book.rating_count }}人评分)</span></p>
      <div class="rating-distribution">
        <div v-for="(percent, star) in ratingDistribution" :key="star" class="rating-bar">
          <span>{{ star }}星</span>
          <div class="bar">
            <div class="fill" :style="{ width: percent + '%' }"></div>
          </div>
          <span>{{ percent }}%</span>
        </div>
      </div>
    </div>
    <div class="description">
      <h2>内容简介</h2>
      <p>{{ book.description }}</p>
    </div>
    <div class="author-info">
      <h2>作者简介</h2>
      <p>{{ book.author_intro }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "BookDetail",
  data() {
    return {
      book: {
        title: "",
        author: "",
        publisher: "",
        publish_date: "",
        pages: "",
        price: "",
        isbn: "",
        rating: "",
        rating_count: "",
        description: "",
        author_intro: "",
        image: "",
        rating_distribution: {}
      }
    };
  },
  computed: {
    bookImage() {
      return require(`@/assets/${this.book.image}`);
    },
    ratingDistribution() {
      return this.book.rating_distribution;
    }
  },
  created() {
    const bookId = this.$route.params.bookId;
    this.book = this.getBookById(bookId);
  },
  methods: {
    getBookById(id) {
      const booksData = require("@/assets/book.json");
      return booksData.find(book => book.id === id);
    }
  }
};
</script>

<style scoped>
.book-detail {
  margin: 20px;
  text-align: left
}
.book-info {
  display: flex;
  margin-bottom: 20px;
}
.book-info img {
  width: 150px;
  height: 200px;
  margin-right: 20px;
}
.details p {
  margin: 5px 0;
}
.rating {
  margin-bottom: 20px;
}
.rating h2 {
  margin-bottom: 10px;
}
.score {
  font-size: 24px;
  font-weight: bold;
}
.rating-distribution {
  margin-top: 10px;
}
.rating-bar {
  display: flex;
  align-items: center;
  margin-bottom: 5px;
}
.rating-bar .bar {
  flex: 1;
  height: 10px;
  background: #eee;
  margin: 0 10px;
  position: relative;
}
.rating-bar .fill {
  height: 100%;
  background: orange;
}
.description, .author-info {
  margin-bottom: 20px;
}
.description h2, .author-info h2 {
  margin-bottom: 10px;
}
</style>
