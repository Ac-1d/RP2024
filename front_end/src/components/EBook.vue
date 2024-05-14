<template>
  <div id="ebook">
    <!-- TODO: 窗口大小溢出，原因未知 -->
    <div id="epub_render"></div>
    <!-- TODO: 弃用蒙版换页，改为按钮换页，但仍需蒙版来放置按钮 -->
    <div id="mask">
      <div id="left" @click="prevPage">点我呼出菜单</div>
      <div id="center" @click="callTable"></div>
      <div id="right" @click="nextPage"></div>
    </div>
    <div id="table" >
      这里是菜单
    </div>
  </div>
</template>

<script>
import Epub from "epubjs"

export default {
  name: "EBook",
  data() {
    return {
      showTable: false
    }
  },
  props: [
    'showNav'
  ],
  mounted() {
    console.log(window.innerWidth, window.innerHeight);
    this.loadEpub();
  },
  methods: {
    loadEpub() {
      this.book = new Epub("books_tmp/09.epub");
      this.rendition = this.book.renderTo("epub_render", {
        width: window.innerWidth,
        height: window.innerHeight
      });
      this.rendition.display();
    },
    prevPage() {
      if(this.rendition) {
        this.rendition.prev();
      }
    },
    nextPage() {
      if(this.rendition) {
        this.rendition.next();
      }
    },
    callTable() {
      this.showTable = !this.showTable;
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
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 100;
    display: flex;
    #left {
      position: relative;
      top: 100;
      left: 100;
    }
  }
  #table {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 100;
    display: flex;
  }
}
</style>