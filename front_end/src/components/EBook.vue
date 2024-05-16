<template>
  <div id="ebook">
    <!-- TODO: 窗口大小溢出，原因未知 -->
    <div id="epub_render"></div>
    <!-- TODO: 弃用蒙版换页，改为按钮换页，但仍需蒙版来放置按钮 -->
    <div id="mask">
      <button id="tableButton" @click="callTable">点我呼出菜单</button>
      <button id="nextPageButton" @click="nextPage">点我向后翻页</button>
      <button id="prevPageButton" @click="prevPage">点我向前翻页</button>
    </div>
    <div id="table" v-if="showTable">
      <div id="bookInfo">这里是书籍信息</div>
      <div id="setting">
        <h1>这里是设置</h1>
        <!-- TODO: 最好改为按下回车/点击页面时修改数值 -->
        调整字体大小：
        <input type="text" v-model="fontSize">
        <div>{{ fontSize }}</div>
        <button id="changeViewStyleButton" @click="changeViewStyle">点我修改视图</button>
        <button @click="test">点我查看代码实现</button>
      </div>
      <div id="progressBar">这里是进度条</div>
    </div>
  </div>
</template>

<script>
import {useEpub} from "../js/Ebook.js";

export default {
  name: "EBook",
  data() {
    return {
      showTable: false,
      fontSize: ''
    }
  },
  props: [
    'showNav'
  ],
  mounted() {
    this.epubReader = useEpub();
    this.loadEpub();
  },
  watch: {
    fontSize(newValue) {
      console.log("call fontSize in watch");
      this.changeFontSize(newValue);
    }
  },
  methods: {
    loadEpub() {
      this.epubReader.createBook("books_tmp/09.epub");
      this.epubReader.render("epub_render", {
        width: window.innerWidth,
        height: window.innerHeight,
        flow: "scrolled-doc"
      });
      this.epubReader.display();
    },
    prevPage() {
      this.epubReader.prevPage();
    },
    nextPage() {
      this.epubReader.nextPage();
    },
    callTable() {
      this.showTable = !this.showTable;
    },
    changeFontSize(fontSize) {
      console.log("call setFontSize");
      this.epubReader.setFontSize(fontSize);
    },
    changeViewStyle() {
      this.epubReader.setViewStyle();
    },
    test() {
      this.epubReader.test();
    }
  },
};
</script>

<style lang="scss" scoped>
#ebook {
  position: relative;
  #epub_render {
    width: 100%;
    height: 100vh;
    justify-content: center;
    align-content: center;
  }
  #mask {
    // position: absolute;
    // top: 0;
    // left: 100;
    // width: 100%;
    // height: 100%;
    // z-index: 90;
    // display: flex;
    #tableButton {
      position: fixed;
      left: 50%;
      transform: translateX(-50%);
      top: 0;
    }
    #nextPageButton {
      position: fixed;
      right: 0;
      bottom: 0;
    }
    #prevPageButton {
      position: fixed;
      left: 0;
      bottom: 0;
    }
  }
  #table {
    // position: absolute;
    // top: 0;
    // left: 0;
    // width: 100%;
    // height: 100%;
    // z-index: 100;
    // display: flex;
    #bookInfo {
      position: fixed;
      top: 0;
      left: 0;
      width: 200px;
      height: 100%;
      background-color: grey;
    }
    #setting {
      position: fixed;
      top: 0;
      right: 0;
      width: 200px;
      height: 100%;
      background-color: grey;
    }
    #progressBar {
      position: fixed;
      align-content: center;
      left: 50%;
      transform: translateX(-50%);
      bottom: 0;
      width: 300px;
      height: 100px;
    }
  }
}
</style>