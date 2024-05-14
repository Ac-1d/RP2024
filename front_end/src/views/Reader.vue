<template>
  <div class="reader">
    <div class="reader-test">
      <div id="read"></div>
      <div class="mask">
        <div class="left" @click="prevPage"></div>
        <div class="center"></div>
        <div class="right" @click="nextPage"></div>
      </div>
      
    </div>
  </div>
</template>

<script>
import Epub from "epubjs";

export default {
  mounted() {
    this.status = false;
    this.loadEpub();
  },
  methods: {
    loadEpub() {
      console.log(this);
      this.showNavbar = false;
      this.book = new Epub("books_tmp/09.epub");
      console.log(this.book);
      this.rendition = this.book.renderTo("read", {
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
    }
  }
};
</script>
<style lang="scss" scoped>
.reader {
  position: relative;
  .reader-test {
    .mask {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: 100;
      display: flex;
      .left {
        flex: 0 0 20%;
      }
      .center {
        flex: 1;
      }
      .right {
        flex: 0 0 20%;
      }
    }
  }
}
</style>