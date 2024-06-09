<template>
  <div class="book-detail">
    <div class="header">
      <div class="title-section">
        <h1>{{ book.title }}</h1>
        <div class="book-info">
          <div class="book-cover" @click="startReading">
            <img :src="bookImage" :alt="book.title" />
          </div>
          <div class="details">
            <p><strong>作者:</strong> {{ book.author }}</p>
            <p><strong>出版社:</strong> {{ book.publisher }}</p>
            <p v-if="book.subtitle"><strong>副标题:</strong> {{ book.subtitle }}</p>
            <p><strong>出版时间:</strong> {{ book.publish_date }}</p>
            <p><strong>页数:</strong> {{ book.pages }}</p>
            <p><strong>定价:</strong> {{ book.price }}</p>
            <p><strong>装帧:</strong> {{ book.binding }}</p>
            <p><strong>ISBN:</strong> {{ book.isbn }}</p>
            <button @click="startReading" class="read-button">阅读</button>
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
        <div class="stars" @mouseleave="resetRating">
          <span v-for="star in 5" :key="star"
                @mouseover="setRating(star)"
                @click="rateBook(star)"
                :class="{'active-star': star <= currentRating, 'inactive-star': star > currentRating}">
            ★
          </span>
        </div>
        <span>{{ ratingText }}</span>
      </div>
    </div>
    <div class="extra-actions">
      <a href="#"><span class="icon">🖊️</span> 写笔记</a>
      <a href="#" @click="linktoComments"><span class="icon">🖊️</span> 写书评</a>
      <a href="#"><span class="icon">¥</span> 加入购物单</a>
      <a href="#"><span class="icon">+</span> 添加到书单</a>
      <a href="#">分享</a>
      <button class="recommend">推荐</button>
    </div>
    <div class="description">
      <h2>内容简介</h2>
      <p>{{ book.description }}</p>
    </div>
    <div class="author-info">
      <h2>作者简介</h2>
      <p>{{ book.author_intro }}</p>
    </div>
    <div class="book-reviews">
      <h2>书籍评论</h2>
      <div v-for="comment in filteredComments" :key="comment.text" class="comment">
        <p><strong>{{ comment.author }}:</strong> {{ comment.text }}</p>
        <p>评分: {{ comment.rank_value }} | 点赞: {{ comment.likes }} | 时间: {{ comment.time }}</p>
      </div>
    </div>
    <div class="book-chapters">
      <h2>章节</h2>
      <ul>
        <li v-for="chapter in chapters" :key="chapter.chapter_id" @click="selectChapter(chapter.chapter_id)">
          {{ chapter.novel_chapter }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex';
import { novelDetail, novelChapter } from '@/js/Api.js'; // 修改大小写以匹配文件名

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
      },
      currentRating: 0,
      finalRating: 0,
      reviews: [], // 评论数据
      chapters: [], // 章节数据
      selectedChapter: null, // 选中的章节号
    };
  },
  computed: {
    bookImage() {
      try {
        return require(`@/assets/${this.book.image}`);
      } catch (e) {
        console.error('Error loading book image:', e);
        return require('@/assets/default-image.png');
      }
    },
    ratingDistribution() {
      return this.book.rating_distribution;
    },
    ratingText() {
      const ratings = ['很差', '较差', '还行', '推荐', '力荐'];
      return ratings[this.currentRating - 1] || '';
    },
    filteredComments() {
      return this.reviews;
    }
  },
  created() {
    const bookId = this.$route.params.bookId;
    this.fetchBookDetails(bookId);
    this.fetchChapters(bookId);
  },
  methods: {
    ...mapActions(['setCurrentBookId', 'setCurrentChapterId']),
    async fetchBookDetails(bookId) {
      try {
        const response = await novelDetail(bookId);
        this.book = response;
        this.finalRating = this.book.rating;
      } catch (error) {
        console.error('Error fetching book details:', error);
      }
    },
    async fetchChapters(bookId) {
      try {
        const response = await novelChapter(bookId);
        this.chapters = response.chapter_data.chapter_list;
      } catch (error) {
        console.error('Error fetching chapters:', error);
      }
    },
    startReading() {
      this.setCurrentBookId(this.book.id);
      this.setCurrentChapterId(1); // 从第一章开始阅读
      this.$router.push({name: 'Reader'});
    },
    linktoComments() {
      this.$router.push({name: 'Comments', params: {bookId: this.book.id}});
    },
    setRating(star) {
      this.currentRating = star;
    },
    resetRating() {
      this.currentRating = this.finalRating;
    },
    rateBook(star) {
      this.finalRating = star;
      this.currentRating = star;
      console.log(`评分为: ${star}`);
    },
    selectChapter(chapterId) {
      this.selectedChapter = chapterId;
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

.book-cover {
  cursor: pointer;
  transition: transform 0.3s ease;
}

.book-cover:hover {
  transform: scale(1.1);
}

.book-info img {
  width: 150px;
  height: 200px;
  margin-right: 20px;
}

.details p {
  margin: 5px 0;
}

.read-button {
  display: block;
  margin-top: 10px;
  padding: 5px 10px;
  background-color: #007bff;
  border: none;
  color: white;
  cursor: pointer;
  border-radius: 5px;
}

.read-button:hover {
  background-color: #0056b3;
}

.rating {
  display: flex;
  align-items: center;
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
  cursor: pointer;
}

.stars .active-star {
  color: orange;
}

.stars .inactive-star {
  color: #ccc;
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

.description, .author-info, .professional-reviews, .table-of-contents, .book-reviews, .book-chapters {
  margin-bottom: 20px;
}

.description h2, .author-info h2, .professional-reviews h2, .table-of-contents h2, .book-reviews h2, .book-chapters h2 {
  margin-bottom: 10px;
}

.table-of-contents ul, .book-chapters ul {
  list-style-type: disc;
  padding-left: 20px;
}

.comment {
  background: #f5f5f5;
  padding: 10px;
  border-radius: 5px;
  margin-bottom: 10px;
}
</style>
