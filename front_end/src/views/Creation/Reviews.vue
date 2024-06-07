<template>
  <div class="home">

    <div class="content">

      <div class="main-content">
        <div class="category-bar">
          <span class="title">作品数据</span>
        </div><div class="separator"></div>

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
import "@/css/layout.css";
export default{
  name: 'Reviews',
}
</script>