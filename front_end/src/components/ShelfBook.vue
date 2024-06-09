<template>
  <div class="book">
    <img :src="book.novel_info.novel_img" :alt="book.novel_info.novel_name" @click="goToRead" @mouseover="showDetails" @mouseleave="hideDetails" />
    <div class="title">{{ book.novel_info.novel_name }}</div>
    <div class="author">{{ book.novel_info.author_namw }}</div>
    <i class="el-icon-remove" @click = "removeBook"></i>

    <transition name="fade">
      <div class="details" v-if="isHovered">
        <h3>{{ book.novel_info.novel_name }}</h3>
        <p><strong>作者:</strong> {{ book.novel_info.author_name }}</p>
        <p><strong>分类:</strong> {{ book.novel_info.category_name }}</p>
        <p><strong>状态:</strong> {{ bookState() }}</p>
        <p><strong>字数:</strong> {{ book.novel_info.total_words }}</p>

        <p><strong>描述:</strong> {{ book.novel_info.novel_detail }}</p>

      </div>
    </transition>
  </div>
</template>

<script>
import axios from 'axios';
import { mapActions } from 'vuex';
export default {
  name: "ShelfBook",
  props: {
    book: {
      type: Object,
      required: true
    },

  },
  data() {
    return {
      isHovered: false
    };
  },

  methods: {
    bookState() {
        console.log("book is"+this.book);
        if(this.book.novel_info.novel_status == 0){
            return "连载中...";
        } else {
            return "已完结";
        }
    },
    showDetails() {
      this.isHovered = true;
    },
    hideDetails() {
      this.isHovered = false;
    },
    ...mapActions(['setCurrentBookId', 'setCurrentChapterId']),
    goToRead() {
      this.$store.commit('setCurrentBookId', this.book.novel_info.id);
      this.$store.commit('setCurrentChapterId', this.book.novel_info.chapter_start);
      this.$router.push({name: 'Reader'});
    },
    removeBook() {
        this.$confirm('确认删除', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.remove();
          this.$message({
            type: 'success',
            message: '删除成功!'
          });
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          });
        });
     },
     remove: async function() {
        console.log('userID'+this.$store.state.userInfo.id);
        console.log('userID'+this.book.novel_info.id);
        try {
            const response = await axios.post('/novels/delete_novel', {
                params: {
                    novel_id: this.book.novel_info.id,
                    user_id: this.$store.state.userInfo.id,
                }
        });

        if (response.status === 200 && response.data.status === 'success') {
          console.log(response.data.msg);
          // 在此处处理成功删除的结果，例如通知用户或刷新列表
        } else {
          console.error('删除失败');
        }
       } catch (error) {
        console.log('------');
        console.error(error);
      }
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
