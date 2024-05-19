<template>
  <div class="center">
    <header class="header">
        <div class="header-content">
            <div class="avatar">
                <img src="@/assets/Avatar.jpg" alt="Avatar" />
            </div>
            <ul class="info" >
            <li class='NickName'><strong>昵称：</strong>{{ nickname }}</li>
                <li class='Level'><strong>等级：</strong>lv{{ level }}</li>
            </ul>

        </div>
    </header>
    <header class="down">
    <aside class="sidebar">
      <ul class='infoSide'>
        <li>性别：{{ sex }}</li>
        <li>手机号：{{ hiddenTele }}</li>
        <li>个性签名：{{ signature }}</li>
      </ul>
    </aside>
    <main class="main">
      <h2>我的书架</h2>
      <!--
      <ul>
        <li v-for="(book, index) in books" :key="index">{{ book.title }}</li>
      </ul>
      -->
    </main>
    </header>
  </div>
</template>

<script>
export default {
   /* components: {
      LoginModal
   }, */
  data() {
    return {
      nickname: "John Doe",
      signature: "好好学习，天天向上!",
      level:"7",
      avatar: "../assets/Avatar.jpg", // 你的头像图片地址
      sex:'男',
      tele:'15513107588'
    };
  },
  computed:{
    hiddenTele(){
        const prefix = this.tele.substring(0, 3);
        const suffix = this.tele.substring(this.tele.length - 2);
        return `${prefix}****${suffix}`;
    },
  },
};
</script>


<style scoped>
:root {
  my_top: 500px;
}
.center {
  display: flex;
  align-items: center;
}

.header {

  position:absolute;
  top:65px;
  left:50px;
  right:50px;
  height:200px;

  background-size: cover;
  background-position: top;
  align-items: center;
  justify-content: center;
  background-color: #f5f5f5;
}
.down {
  position:absolute;
  top:265px;
  left:50px;
  right:50px;
  height:450px;
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
  top:0px;
  left:0px;
  width:200px;
  height:100%;
  background-color: #f5f5f5;
}
.infoSide{
  list-style-type: none;
  position:absolute;
  top:10px;

}
.main {
  position:absolute;
  top:0px;
  left:200px;
  right:0px;
  height:100%;
  background-color: yellow;
}

.info {
  list-style-type: none;
  position:absolute;
  bottom:10px;
  left:210px;
}

li {
  margin-bottom: 10px;
}
</style>
