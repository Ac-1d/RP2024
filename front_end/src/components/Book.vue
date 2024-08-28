<template>
  <div class="book">
    <img :src="bookImage" :alt="book.novel_name" @click="goToDetailPage" @mouseover="showDetails" @mouseleave="hideDetails" />
    <div class="title">{{ book.novel_name }}</div>
    <div class="author">{{ book.author_name }}</div>
    <transition name="fade">
      <div class="details" v-if="isHovered">
        <h3>{{ book.novel_name }}</h3>
        <p><strong>作者:</strong> {{ book.author_name }}</p>
        <p><strong>分类:</strong> {{ book.category_name }}</p>
        <p><strong>出版社:</strong> {{ book.publisher }}</p>
        <p><strong>出版时间:</strong> {{ book.publish_date }}</p>
        <p><strong>页数:</strong> {{ book.pages }}</p>
        <p><strong>价格:</strong> {{ book.price }}</p>
        <p><strong>ISBN:</strong> {{ book.isbn }}</p>
        <p><strong>描述:</strong> {{ book.novel_detail }}</p>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  name: "Book",
  props: {
    book: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      isHovered: false
    };
  },
  computed: {
    bookImage() {
      console.log(this.book.novel_img.split('http://127.0.0.1:8000/')[1])
      return this.book.novel_img.split('http://127.0.0.1:8000/')[1];
      // return require('@/assets/default.jpg');
    }
  },
  methods: {
    showDetails() {
      this.isHovered = true;
    },
    hideDetails() {
      this.isHovered = false;
    },
    goToDetailPage() {
      this.$router.push({name: 'BookDetail', params: {bookId: this.book.id}});
    }
  }
};
</script>

<style scoped>
.book {
  text-align: center;
  margin: 10px;
  position: relative;
  width: 150px;
}

.book img {
  width: 100px;
  height: 150px;
  cursor: pointer;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s;
}

.book img:hover {
  transform: scale(1.05);
}

.title {
  font-weight: bold;
  margin-top: 10px;
  font-size: 14px;
  color: #333;
}

.author {
  color: #777;
  margin-top: 5px;
  font-size: 12px;
}

.details {
  position: absolute;
  top: 0;
  left: 160px;
  width: 300px;
  background: white;
  border: 1px solid #ccc;
  padding: 15px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  z-index: 10;
  font-size: 14px;
  color: #333;
  border-radius: 5px;
  font-family: 'Arial', sans-serif;
  text-align: left;
}

.details h3 {
  font-size: 18px;
  margin-bottom: 10px;
  color: #444;
}

.details p {
  margin: 8px 0;
  line-height: 1.5;
}

.details strong {
  color: #555;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s;
}

.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>
