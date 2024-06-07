<template>
  <div class="categories-detail">
    <h1 class="title">新书速递</h1>
    <ul class="categories">
      <li :class="{ active: selectedCategory === '全部' }" @click="filterBooks('全部')">全部</li>
      <li :class="{ active: selectedCategory === '文学' }" @click="filterBooks('文学')">文学</li>
      <li :class="{ active: selectedCategory === '小说' }" @click="filterBooks('小说')">小说</li>
      <li :class="{ active: selectedCategory === '历史文化' }" @click="filterBooks('历史文化')">历史文化</li>
      <li :class="{ active: selectedCategory === '社会纪实' }" @click="filterBooks('社会纪实')">社会纪实</li>
      <li :class="{ active: selectedCategory === '科学新知' }" @click="filterBooks('科学新知')">科学新知</li>
      <li :class="{ active: selectedCategory === '艺术设计' }" @click="filterBooks('艺术设计')">艺术设计</li>
      <li :class="{ active: selectedCategory === '商业经管' }" @click="filterBooks('商业经管')">商业经管</li>
      <li :class="{ active: selectedCategory === '绘本漫画' }" @click="filterBooks('绘本漫画')">绘本漫画</li>
    </ul>
    <div class="book-list">
      <div class="book-item" v-for="book in filteredBooks" :key="book.id" @click="goToBookDetail(book.id)">
        <img :src="require(`@/assets/${book.image}`)" :alt="book.title" class="book-image" />
        <div class="book-info">
          <h2 class="book-title">{{ book.title }}</h2>
          <p class="book-author">{{ book.author }} / {{ book.publish_date }} / {{ book.publisher }} / {{ book.price }}</p>
          <p class="book-rating">
            <span class="rating-stars">{{ renderStars(book.rating) }}</span>
            <span class="rating-score">{{ book.rating }}</span> ({{ book.rating_count }}人评价)
          </p>
        </div>
        <div class="book-actions">
          <a href="#" class="book-link">纸质版 {{ book.price }}</a>
          <a href="#" class="book-link">加入购物单</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'; // 导入 axios

export default {
  name: "CategoriesDetail",
  data() {
    return {
      books: [], // 初始为空数组
      selectedCategory: "全部" // 当前选中的分类
    };
  },
  computed: {
    filteredBooks() {
      if (this.selectedCategory === "全部") {
        return this.books;
      }
      return this.books.filter(book => book.category === this.selectedCategory);
    }
  },
  methods: {
    async fetchBooks() {
      try {
        const response = await axios.get('/api/books'); // 假设你的后端API路径是 /api/books
        this.books = response.data;
      } catch (error) {
        console.error('Error fetching books:', error);
      }
    },
    filterBooks(category) {
      this.selectedCategory = category;
    },
    renderStars(rating) {
      const stars = Math.round(rating / 2); // 将评分转换为5颗星的比例
      return "★".repeat(stars) + "☆".repeat(5 - stars); // 返回星星字符
    },
    goToBookDetail(bookId) {
      this.$router.push({ name: 'BookDetail', params: { bookId } });
    }
  },
  created() {
    this.fetchBooks(); // 在组件创建时获取书籍数据
  }
};
</script>

<style scoped>
.categories-detail {
  padding: 20px;
  max-width: 700px; /* 限制内容区域的最大宽度 */
  margin: 0 auto; /* 居中对齐 */
}

.title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
}

.categories {
  display: flex;
  flex-wrap: wrap;
  padding: 8px; /* 内边距 */
  list-style: none;
  margin-bottom: 20px;
  background-color: #e6e2dd; /* 淡黄色背景 */
}

.categories li {
  margin-right: 15px;
  color: gray;
  cursor: pointer;
}

.categories li.active {
  font-weight: bold;
  color: black;
}

.book-list {
  display: flex;
  flex-direction: column;
  min-height: 500px; /* 固定最小高度，减少内容高度变化引起的抖动 */
}

.book-item {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
  width: 100%;
  border: 1px solid #ccc; /* 添加边框 */
  border-radius: 5px; /* 边框圆角 */
  padding: 10px; /* 添加内边距 */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* 添加阴影效果 */
  cursor: pointer; /* 鼠标变为手型 */
  transition: transform 0.3s ease; /* 添加过渡效果 */
}

.book-item:hover {
  transform: scale(1.05); /* 放大效果 */
}

.book-image {
  width: 80px;
  height: 120px;
  margin-right: 20px;
}

.book-info {
  text-align: left; /* 将文本左对齐 */
  flex-grow: 1;
}

.book-title {
  font-size: 20px;
  color: #0b5278;
  margin: 0;
}

.book-author {
  font-size: 16px;
  color: #757575;
  margin: 12px 0;
}

.book-rating {
  font-size: 14px;
  color: #757575;
  margin: 5px 0;
}

.rating-stars {
  color: #FFD596;
}

.rating-score {
  font-weight: bold;
  color: rgba(197, 20, 20, 0.65);
}

.book-actions {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
}

.book-link {
  font-size: 14px;
  color: #4890af;
  margin-top: 5px;
  text-decoration: none;
}

.book-link:hover {
  text-decoration: underline;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s;
}

.fade-enter, .fade-leave-to /* .fade-leave-active in <2.1.8 */ {
  opacity: 0;
}
</style>
