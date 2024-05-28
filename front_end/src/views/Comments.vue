<template>
  <div class="comments">
    <h1>写书评</h1>
    <textarea v-model="reviewContent"></textarea>
    <button @click="submitReview">提交书评</button>
  </div>
</template>

<script>
import { EventBus } from '@/utils/eventBus'; // 引入事件总线

export default {
  name: "Comments",
  data() {
    return {
      reviewContent: ''
    };
  },
  methods: {
    submitReview() {
      const bookId = this.$route.params.bookId;
      const newReview = {
        id: Date.now(),
        bookId: bookId,
        content: this.reviewContent
      };
      EventBus.$emit('newReview', newReview); // 发送新评论事件
      this.$router.go(-1); // 关闭评论页面，返回上一页
    }
  }
};
</script>

<style scoped>
.comments {
  margin: 20px auto;
  max-width: 800px;
  text-align: left;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 5px;
  background-color: #f9f9f9;
}

textarea {
  width: 100%;
  height: 200px;
  margin-bottom: 20px;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
}

button {
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>
