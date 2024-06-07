<template>
  <div class="home">
    <!-- 中部导航栏 -->
    <!-- <MiddleNavBar /> -->

    <div class="content">
      <!-- 功能栏 -->
      <!-- <SideBar /> -->

      <div class="main-content">
        <div class="category-bar">
          <span class="title">我的作品</span>
        </div><div class="separator"></div>

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
// import MiddleNavBar from "@/components/MiddleNavBar.vue"; // 引用 MiddleNavBar 组件
// import SideBar from "@/components/SideBar.vue"; // 引用 SideBar 组件
import booksData from "@/assets/book.json"; // 导入本地的 books.json 文件
import "@/css/layout.css";

export default {
  name: "Home",
  components: {
    Book,
    // MiddleNavBar, // 注册 MiddleNavBar 组件
    // SideBar // 注册 SideBar 组件
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
