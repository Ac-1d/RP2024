<template>
  <div class="center">
    <header class="header">
        <div class="header-content">
            <div class="avatar">
                <img :src="userInfo.avatar_path" alt="Avatar" />
            </div>
            <ul class="info" >
            <li class='NickName'><strong>昵称：</strong>{{ userInfo.nickName }}</li>
                <li class='Level'><strong>等级：</strong>lv{{ userInfo.level }}</li>
            </ul>

        </div>
    </header>
    <header class="down">
    <aside class="sidebar">
      <ul class='infoSide'>
        <li><h1>资料卡片:</h1></li>
        <li><strong>性别：</strong>{{ userInfo.sex || '暂未选择' }}</li>
        <li><strong>出生日期：</strong>{{ formattedBirth || '暂未填写' }}</li>
        <li><strong>手机号：<br/></strong>{{ hiddenTele }}</li>
        <li><strong>个性签名：<br/></strong>{{ userInfo.signature || '暂未填写'}}</li>
        <br>
        <li>
        <el-button @click="showModi = true" type="primary" plain >
            修改个人信息
        </el-button>
        </li>
      </ul>
    </aside>
    <main class="main">

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

    </main>
    </header>
    <Modify_info :drawer="showModi" :ruleForm="userInfo" @closedia="showModi = false" @send = "changeModify"></Modify_info>
  </div>
</template>

<script>
import ShelfBook from "@/components/ShelfBook.vue";
import booksData from "@/assets/book.json"; // 导入本地的 books.json 文件
import Modify_info from "@/components/Modify_information.vue";

export default {
  components: {
      ShelfBook,
      Modify_info,
  },

  data() {
    return {
      books:booksData,
      userInfo:{
          "ID": "U88965",
          "avatar_path":"https://p2.ssl.qhimgs1.com/t047799700da192d488.jpg",
          "level": 7,
          "nickName": "pizza_k9999",
          "sex": "女",
          "birth": new Date('2004-07-13'),
          "signature": "",
          "tele":"15513107588",
          "password":'59jkb2h0',
      },
      showModi: false,
      currentPage: 1, // 当前页码
      booksPerPage: 12, // 每页显示的书籍数量
    };
  },

  created() {
    console.log(this.userInfo.nickName);
    console.log(this.$store.state.userInfo);
    this.userInfo.ID = this.$store.state.userInfo.id;
    // this.userInfo.avatar_path = this.$store.state.userInfo.user_icon;
    this.userInfo.sex = this.$store.state.userInfo.gender;
    this.userInfo.password = this.$store.state.userInfo.password;
    this.userInfo.nickName = this.$store.state.userInfo.username;

    let dateObj = new Date(this.$store.state.userInfo.birth_date);
    let formattedDate = dateObj.toISOString().split('T')[0];
    let birth = new Date(formattedDate);
    this.userInfo.birth = birth;

    this.userInfo.signature = this.$store.state.userInfo.signature;
    this.userInfo.tele = this.$store.state.userInfo.mobile;
    console.log(this.userInfo.nickName);
  },

  methods:{
      changeModify(newInfo){
        this.userInfo.nickName = newInfo.nickName;
        this.userInfo.sex = newInfo.sex;
        this.userInfo.signature = newInfo.signature;
        this.userInfo.birth = newInfo.birth;
        console.log('center'+this.userInfo.nickName);
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
    hiddenTele(){
        console.log('TeleBegin');
        const prefix = this.userInfo.tele.substring(0, 3);
        const suffix = this.userInfo.tele.substring(this.userInfo.tele.length - 2);
        console.log('TeleEnd');
        return `${prefix}****${suffix}`;

    },
    formatNumber(n) { // 辅助函数，用于补零操作，确保月份和日期始终为两位数
      n = n.toString();
      return n[1] ? n : '0' + n;
    },

    formattedBirth() {
      let temp;
      console.log("---");
      console.log(this.userInfo.birth);
      console.log(this.userInfo.birth instanceof Date);
      const year = this.userInfo.birth.getFullYear();
      temp = this.userInfo.birth.getMonth() + 1;// 月份是从0开始的，所以需要+1
      temp = temp.toString();
      const month = temp[1] ? temp : '0' +temp ;
      temp = this.userInfo.birth.getDate() ;
      temp = temp.toString();
      const day = temp[1] ? temp : '0' +temp ;
      return `${year}.${month}.${day}`;
    },
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
.center {
  display: flex;
  flex-direction: column ;
  align-items: center;
  height: 100vh;
}

.header {

  background-image: url('../assets/center_back.jpg');
  flex: 0 0 30%; /* 高度固定为30%，不可伸缩 */
  margin-top: 0.3%;
  margin-bottom: 0.3%;
  width: 90%;

  background-size: cover;
  background-position: top;

  color: #333; /* 设置字体颜色 */
  text-align: left;
  color: black;

  position: relative;
}
.down {
  flex: 1; /* 剩余空间均分给底部容器 */
  display: flex; /* 底部容器也需要是Flex布局来安排左右组件 */
  justify-content: space-between; /* 左右两侧分别靠边，中间自然间隔 */
  padding: 0 5%; /* 左右边界各留5%的间距 */
}


.avatar {
  position: absolute;
  left: 8%;
  top: 40%;
  width: 110px;
  height: 110px;
  border-radius: 50%;
  object-fit: cover;
  margin-bottom: 10px;
}

.avatar img {
  border-radius: 45%;
  width: 120px;
  height: 120px;
  object-fit: cover;
  border: 3px solid rgba(170, 110, 140, 0.3);

}
.NickName {
    font-size:30px;
}
.Level {
    font-size:20px;
}
.sidebar {
  flex: 0 0 18%;
  background-color: #f5f5f5;
  margin-right: 3%;
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
  margin-right: 10%;
  margin-left: 3%;
  text-align: left; /* 设置左对齐 */
  line-height: 30px; /* 设置行距为15px */
  padding:20px;
}
.main {
  flex:1;
  background-color: #fff;
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start; /* 左对齐 */
}

.info {
  position: relative; /* 文本相对于其正常流位置定位 */
  top:90%;

  margin-top: 10%;
  margin-left: 20%;
  list-style-type: none;
  color: #555; /* 设置字体颜色 */
  font-weight: bold;
}

strong{
color: #333; /* 设置加粗字体颜色 */
}
</style>
