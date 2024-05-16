<template>
  <div class="book" @mouseover="showDetails" @mouseleave="hideDetails">
    <img :src="bookImage" :alt="book.title" @click="goToDetailPage" />
    <div class="title">{{ book.title }}</div>
    <div class="author">{{ book.author }}</div>
    <transition name="fade">
      <div class="details" v-if="isHovered">
        <h3>{{ book.title }}</h3>
        <p><strong>作者:</strong> {{ book.author }}</p>
        <p><strong>分类:</strong> {{ book.category }}</p>
        <p><strong>出版社:</strong> {{ book.publisher }}</p>
        <p><strong>出版时间:</strong> {{ book.publish_date }}</p>
        <p><strong>页数:</strong> {{ book.pages }}</p>
        <p><strong>价格:</strong> {{ book.price }}</p>
        <p><strong>ISBN:</strong> {{ book.isbn }}</p>
        <p><strong>描述:</strong> {{ book.description }}</p>
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
      return require(`@/assets/${this.book.image}`);
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
      this.$router.push({ name: 'BookDetail', params: { bookId: this.book.id } });
    }
  }
};
</script>

<style scoped>
.book {
  text-align: center;
  margin: 10px;
  position: relative; /* 确保 .book 元素是相对定位的，以便详情框可以相对于它定位 */
  width: 150px; /* 限制每本书的宽度 */
}
.book img {
  width: 100px; /* 调整图片大小 */
  height: 150px; /* 调整图片大小 */
  cursor: pointer;
  border-radius: 5px; /* 圆角效果 */
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* 增加阴影效果 */
  transition: transform 0.3s; /* 增加放大效果 */
}
.book img:hover {
  transform: scale(1.05); /* 放大效果 */
}
.title {
  font-weight: bold;
  margin-top: 10px;
  font-size: 14px; /* 调整字体大小 */
  color: #333;
}
.author {
  color: #777;
  margin-top: 5px;
  font-size: 12px; /* 调整字体大小 */
}
.details {
  position: absolute; /* 确保详情框是绝对定位的 */
  top: 0;
  left: 160px; /* 根据需要调整位置 */
  width: 300px; /* 增加宽度 */
  background: white; /* 设置背景颜色 */
  border: 1px solid #ccc;
  padding: 15px; /* 增加内边距 */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 增加阴影效果 */
  z-index: 10; /* 确保详情框在所有其他元素之上 */
  font-size: 14px; /* 设置字体大小 */
  color: #333; /* 设置字体颜色 */
  border-radius: 5px; /* 增加圆角 */
  font-family: 'Arial', sans-serif; /* 设置字体 */
  text-align: left; /* 左对齐文本 */
}
.details h3 {
  font-size: 18px; /* 设置标题字体大小 */
  margin-bottom: 10px;
  color: #444; /* 设置标题颜色 */
}
.details p {
  margin: 8px 0; /* 增加段落间距 */
  line-height: 1.5; /* 设置行高 */
}
.details strong {
  color: #555; /* 设置加粗字体颜色 */
}
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active in <2.1.8 */ {
  opacity: 0;
}
</style>
