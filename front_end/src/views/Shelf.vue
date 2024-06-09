<template>
    <div class="main">
     <ShelfBook
         v-for="book in paginatedBooks"
         :key="book.title"
         :book="book"
         :novelId="book.id"
     />

        <!-- 翻页栏 -->
        <div class="pagination">
          <button @click="prevPage" :disabled="currentPage === 1">&lt;</button>
          <span v-for="page in totalPages" :key="page" :class="['page-dot', { active: page === currentPage }]" @click="goToPage(page)"></span>
          <button @click="nextPage" :disabled="currentPage === totalPages">&gt;</button>
        </div>

  </div>
</template>

<script>
import axios from 'axios';
import ShelfBook from "@/components/ShelfBook.vue";
//import booksData from "@/assets/book.json"; // 导入本地的 books.json 文件


export default {

  components: {
      ShelfBook,
  },
  props: {
      mode:Number,
  },

  data() {
    return {
      books: [],
      currentPage: 1, // 当前页码
      booksPerPage: 21, // 每页显示的书籍数量
    };
  },

  created() {
    console.log("grwraesvr");
    this.getBookShelfL();
  },
  methods:{
    getBookShelfL: async function(){
        try {
            const response = await axios.get('/novels/bookrack', {
              params: {
                user_id: this.$store.state.userInfo.id,
                sort: 'preference'
              }
            });
            console.log(response);
            this.books = response.data.bookrack;
        }catch(error) {
            console.log(error);
        }
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


  },

  computed:{

    totalPages() {
      return Math.ceil(this.books.length / this.booksPerPage);
    },
    paginatedBooks() {
      const start = (this.currentPage - 1) * this.booksPerPage;
      const end = start + this.booksPerPage;
      return this.books.slice(start, end);
    }
  },
};
</script>


<style scoped>

.main {
  flex:1;
  background-color: #fff;
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start; /* 左对齐 */
}


</style>
