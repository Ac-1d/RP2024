<template>
  <div class="center">
    <header class="header">
        <div class="header-content">
            <div class="avatar">
                <img src="@/assets/Avatar.jpg" alt="Avatar" />
            </div>
            <ul class="info" >
            <li class='NickName'><strong>昵称：</strong>{{ user.nickname }}</li>
                <li class='Level'><strong>等级：</strong>lv{{ user.level }}</li>
            </ul>

        </div>
    </header>
    <header class="down">
    <aside class="sidebar">
      <ul class='infoSide'>
        <li><h1>资料卡片:</h1></li>
        <li><strong>性别：</strong>{{ user.sex }}</li>
        <li><strong>手机号：<br/></strong>{{ hiddenTele }}</li>
        <li><strong>个性签名：<br/></strong>{{ user.signature }}</li>
        <br>
        <li>
        <el-button @click="showModi = true" type="primary" plain >
            修改个人信息
        </el-button>
        </li>
      </ul>
    </aside>
    <main class="main">
      <Book v-for="book in paginatedBooks" :key="book.title" :book="book" />
    </main>
    </header>
    <Modify_info :drawer="showModi" @closedia="showModi = false"></Modify_info>
  </div>
</template>

<script>
import Book from "@/components/Book.vue";
import booksData from "@/assets/book.json"; // 导入本地的 books.json 文件
import Modify_info from "@/components/Modify_information.vue";

export default {
   components: {
      Book,
      Modify_info,
   },
  data() {
    return {
      books:booksData,
      user:{
         "ID": "U88965",
         "level": 7,
         "nickname": "pizza_k",
         "sex": "女",
         "signature": "远方，就是我站立的地方",
         "tele":"15513107588"
      },
      showModi: false,
    };
  },

  computed:{
    hiddenTele(){
        const prefix = this.user.tele.substring(0, 3);
        const suffix = this.user.tele.substring(this.user.tele.length - 2);
        return `${prefix}****${suffix}`;
    },
    paginatedBooks() {
    // 假设你有一个分页逻辑，这里简单返回全部书籍作为示例
    return this.books;
    },
  },
};
</script>


<style scoped>
.center {
  display: flex;
  align-items: center;

}

.header {
  background-image: url('../assets/center_back.jpg');
  position:absolute;
  top:65px;
  left:50px;
  right:50px;
  height:200px;

  background-size: cover;
  background-position: top;

  color: #333; /* 设置字体颜色 */
}
.down {
  position:absolute;
  top:265px;
  left:50px;
  right:50px;
  height:430px;
}

.header-content {
  text-align: left;
  color: black;
}
.avatar {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  object-fit: cover;
  margin-bottom: 10px;
}

.avatar img {
  position:absolute;
  bottom:30px;
  left:100px;
  border-radius: 45%;
  width: 110px;
  height: 110px;
  object-fit: cover;
}
.NickName {
    font-size:30px;
}
.Level {
    font-size:20px;
}
.sidebar {
  position:absolute;
  top:2px;
  left:0px;
  width:200px;
  height:100%;
  background-color: #f5f5f5;

  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5); /* 增加阴影效果 */
  font-size: 14px; /* 设置字体大小 */
  color: #333; /* 设置字体颜色 */
  border-radius: 5px; /* 增加圆角 */
  font-family: 'Arial', sans-serif; /* 设置字体 */
  text-align: left; /* 左对齐文本 */
}
.infoSide{
  color: #555; /* 设置字体颜色 */
  list-style-type: none;
  position:absolute;
  top:20px;
  left:0px;
  right:30px;
  text-align: left; /* 设置左对齐 */
  line-height: 30px; /* 设置行距为15px */
}
.main {
  position:absolute;
  top:2px;
  left:205px;
  right:0px;
  height:100%;
  background-color: #fff;
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start; /* 左对齐 */
}

.info {
  list-style-type: none;
  position:absolute;
  bottom:10px;
  left:210px;
  color: #555; /* 设置字体颜色 */
  font-weight: bold;
}

strong{
color: #333; /* 设置加粗字体颜色 */
}
</style>
