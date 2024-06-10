<template>
  <div class="home">

    <div class="content">

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
import {authorInfo} from '@/js/Api.js';
import "@/css/layout.css";

export default {
  name: "Home",
  components: {
    Book,
  },
  async created() {
    await this.getInfo();
  },
  data() {
    return {
      books: [], 
      currentPage: 1, // 当前页码
      booksPerPage: 12, // 每页显示的书籍数量
      authorInfo: null,
    };
  },
  computed: {
    totalPages() {
      return Math.ceil(this.books.length / this.booksPerPage);
    },
    paginatedBooks() {
      const start = (this.currentPage - 1) * this.booksPerPage;
      const end = start + this.booksPerPage;
      return this.books.slice(start, end);
    }
  },
  methods: {
    async getInfo() {
      const user_id = this.$store.state.userInfo.id;
      const info = await authorInfo(user_id);
      // console.log('info:');
      // console.log(info);
      this.authorInfo = info;
      this.books = info.author_info.related_novels;
      // console.log(this.books);
    },
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
    goToCategoriesDetail() {
      this.$router.push({ name: 'CategoriesDetail' });
    }
  }
};
</script>
