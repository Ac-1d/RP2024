<template>
  <div class="home">
<!--    &lt;!&ndash; 顶级导航栏 &ndash;&gt;-->
<!--    <TopNavBar />-->

    <!-- 中间导航栏 -->
    <MiddleNavBar />

    <!-- 底部导航栏 -->
    <div class="bottom-nav-bar">
      <router-link to="/bookshelf">购书单</router-link>
      <router-link to="/ebooks">电子图书</router-link>
      <router-link to="/rankings">2023年度榜单</router-link>
      <router-link to="/reports">2023年度报告</router-link>
    </div>

    <!-- 顶部分类栏 -->
    <div class="category-bar">
      <span class="title">新书速递</span>
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
        <li><a href="#">更多&gt;&gt;</a></li>
      </ul>
    </div>
    <div class="separator"></div>

    <!-- 书籍展示区域 -->
    <div class="books">
      <Book v-for="book in paginatedBooks" :key="book.title" :book="book" />
    </div>

    <!-- 翻页栏 -->
    <div class="pagination">
      <button @click="prevPage" :disabled="currentPage === 1">&lt;</button>
      <span v-for="page in totalPages" :key="page" :class="['page-dot', { active: page === currentPage }]" @click="goToPage(page)"></span>
      <button @click="nextPage" :disabled="currentPage === totalPages">&gt;</button>
    </div>
  </div>
</template>

<script>
// import TopNavBar from "@/components/TopNavBar.vue";
import MiddleNavBar from "@/components/MiddleNavBar.vue";
import Book from "@/components/Book.vue";
import booksData from "@/assets/book.json"; // 导入本地的 books.json 文件

export default {
  name: "Home",
  components: {
    // TopNavBar,
    MiddleNavBar,
    Book
  },
  data() {
    return {
      books: booksData, // 使用本地的 books.json 数据
      currentPage: 1, // 当前页码
      booksPerPage: 10, // 每页显示的书籍数量
      selectedCategory: "全部", // 当前选中的分类
      query: "" // 搜索查询
    };
  },
  computed: {
    filteredBooks() {
      if (this.selectedCategory === "全部") {
        return this.books;
      }
      return this.books.filter(book => book.category === this.selectedCategory);
    },
    totalPages() {
      return Math.ceil(this.filteredBooks.length / this.booksPerPage);
    },
    paginatedBooks() {
      const start = (this.currentPage - 1) * this.booksPerPage;
      const end = start + this.booksPerPage;
      return this.filteredBooks.slice(start, end);
    }
  },
  methods: {
    prevPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
      }
    },
    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++;
      }
    },
    goToPage(page) {
      this.currentPage = page;
    },
    filterBooks(category) {
      this.selectedCategory = category;
      this.currentPage = 1; // 重置到第一页
    },
    search() {
      if (this.query.trim()) {
        this.$router.push({name: 'Search', query: {q: this.query, c:2}});
      }
    }
  }
};
</script>

<style scoped>
.home {
  text-align: center;
}

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

.bottom-nav-bar {
  display: flex;
  justify-content: center;
  padding: 10px 0;
  background-color: #f8f8f8;
  border-bottom: 1px solid #ddd;
}

.bottom-nav-bar a {
  margin-right: 15px;
  color: #555;
  text-decoration: none;
}

.bottom-nav-bar a:hover {
  text-decoration: underline;
}

/* 顶部分类栏样式 */
.category-bar {
  text-align: left;
  padding: 20px;
}

.category-bar .title {
  font-weight: bold;
  font-size: 20px;
  margin-right: 20px;
}

.category-bar .categories {
  display: inline-block;
  padding: 0;
  list-style: none;
}

.category-bar .categories li {
  display: inline;
  margin-right: 15px;
  color: gray;
  cursor: pointer;
}

.category-bar .categories li.active {
  font-weight: bold;
  color: black;
}

.category-bar .categories li a {
  color: blue;
  text-decoration: none;
}

.category-bar .categories li a:hover {
  text-decoration: underline;
}

.separator {
  width: 100%;
  height: 1px;
  background-color: lightgray;
  margin: 10px 0;
}

/* 书籍展示区域样式 */
.books {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start; /* 左对齐 */
}

/* 翻页栏样式 */
.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
  position: fixed; /* 固定位置 */
  bottom: 20px; /* 距离底部 */
  left: 50%; /* 水平居中 */
  transform: translateX(-50%);
  background: white;
  padding: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  border-radius: 5px;
}

.pagination button {
  background: none;
  border: none;
  font-size: 20px;
  cursor: pointer;
}

.pagination .page-dot {
  width: 10px;
  height: 10px;
  background-color: lightgray;
  border-radius: 50%;
  margin: 0 5px;
  cursor: pointer;
}

.pagination .page-dot.active {
  background-color: gray;
}
</style>
