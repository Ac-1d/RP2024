<template>
  <div class="home">
    <!-- 中部导航栏 -->
    <MiddleNavBar />

    <div class="content">
      <!-- 功能栏 -->
      <SideBar />

      <div class="main-content">
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
            <li><a href="#" @click.prevent="goToCategoriesDetail">更多&gt;&gt;</a></li>
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
    </div>
  </div>
</template>

<script>
import Book from "@/components/Book.vue";
import MiddleNavBar from "@/components/MiddleNavBar.vue"; // 引用 MiddleNavBar 组件
import SideBar from "@/components/SideBar.vue"; // 引用 SideBar 组件
import booksData from "@/assets/book.json"; // 导入本地的 books.json 文件

export default {
  name: "Home",
  components: {
    Book,
    MiddleNavBar, // 注册 MiddleNavBar 组件
    SideBar // 注册 SideBar 组件
  },
  data() {
    return {
      books: booksData, // 使用本地的 books.json 数据
      currentPage: 1, // 当前页码
      booksPerPage: 12, // 每页显示的书籍数量
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
    },
    goToCategoriesDetail() {
      this.$router.push({ name: 'CategoriesDetail' });
    }
  }
};
</script>

<style scoped>
.home {
  text-align: center;
}

.content {
  display: flex;
}

/* 功能栏样式 */
.side-bar {
  flex: 0 0 200px; /* 固定宽度 */
}

/* 主内容区域样式 */
.main-content {
  flex: 1;
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
