<template>
  <div class="book-detail">
    <div class="header">
      <div class="title-section">
        <h1>{{ book.title }}</h1>
        <div class="book-info">
          <img :src="bookImage" :alt="book.title" />
          <div class="details">
            <p><strong>作者:</strong> {{ book.author }}</p>
            <p><strong>出版社:</strong> {{ book.publisher }}</p>
            <p v-if="book.subtitle"><strong>副标题:</strong> {{ book.subtitle }}</p>
            <p><strong>出版时间:</strong> {{ book.publish_date }}</p>
            <p><strong>页数:</strong> {{ book.pages }}</p>
            <p><strong>定价:</strong> {{ book.price }}</p>
            <p><strong>装帧:</strong> {{ book.binding }}</p>
            <p><strong>ISBN:</strong> {{ book.isbn }}</p>
          </div>
        </div>
      </div>
      <div class="rating-section">
        <h2>豆瓣评分</h2>
        <div class="score">{{ book.rating }} <span>({{ book.rating_count }}人评分)</span></div>
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
    </div>
    <div class="actions">
      <button class="read-status">想读</button>
      <button class="read-status">在读</button>
      <button class="read-status">读过</button>
      <div class="rating">
        <span>评价:</span>
        <span class="stars">★★★★★</span>
      </div>
    </div>
    <div class="extra-actions">
      <a href="#"><span class="icon">🖊️</span> 写笔记</a>
      <a href="#"><span class="icon">🖊️</span> 写书评</a>
      <a href="#"><span class="icon">¥</span> 加入购物单</a>
      <a href="#"><span class="icon">+</span> 添加到书单</a>
      <a href="#">分享</a>
      <button class="recommend">推荐</button>
    </div>
    <div class="description">
      <h2>内容简介</h2>
      <p>{{ book.description }}</p>
    </div>
    <div class="professional-reviews" v-if="book.professional_reviews">
      <h2>专业评论</h2>
      <p>{{ book.professional_reviews }}</p>
    </div>
    <div class="author-info">
      <h2>作者简介</h2>
      <p>{{ book.author_intro }}</p>
    </div>
    <div class="table-of-contents" v-if="book.table_of_contents">
      <h2>目录</h2>
      <ul>
        <li v-for="(item, index) in book.table_of_contents" :key="index">{{ item }}</li>
      </ul>
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
        subtitle: "",
        publish_date: "",
        pages: "",
        price: "",
        binding: "",
        isbn: "",
        rating: "",
        rating_count: "",
        description: "",
        author_intro: "",
        image: "",
        rating_distribution: {},
        professional_reviews: "",
        table_of_contents: []
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
  margin: 20px auto;
  max-width: 800px;
  text-align: left;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 5px;
  background-color: #f9f9f9;
}

.header {
  display: flex;
  justify-content: space-between;
}

.title-section {
  flex: 2;
}

.rating-section {
  flex: 1;
  text-align: center;
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

.actions, .extra-actions {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.read-status {
  margin-right: 10px;
  padding: 5px 10px;
  background-color: #f0f0f0;
  border: 1px solid #ddd;
  border-radius: 5px;
}

.rating {
  display: flex;
  align-items: center;
}

.rating span {
  margin-right: 5px;
}

.stars {
  color: #ff9900;
}

.extra-actions a {
  margin-right: 10px;
  text-decoration: none;
  color: #007bff;
}

.extra-actions .icon {
  margin-right: 5px;
}

.extra-actions .recommend {
  padding: 5px 10px;
  background-color: #dff0d8;
  border: 1px solid #d6e9c6;
  border-radius: 5px;
  color: #3c763d;
}

.description, .author-info, .professional-reviews, .table-of-contents {
  margin-bottom: 20px;
}

.description h2, .author-info h2, .professional-reviews h2, .table-of-contents h2 {
  margin-bottom: 10px;
}

.table-of-contents ul {
  list-style-type: disc;
  padding-left: 20px;
}
</style>
