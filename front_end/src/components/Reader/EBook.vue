<template>
  <div id="ebook">
    <div id="epub_render"></div>
    <div id="mask">
      <div id="left" @click="prevPage"></div>
      <div id="center"></div>
      <div id="right" @click="nextPage"></div>
    </div>
  </div>
</template>

<script>
import Epub from "epubjs"

export default {
  name: "EBook",
  mounted() {
    this.loadEpub();
  },
  methods: {
    loadEpub() {
      console.log(this);
      this.showNavbar = false;
      this.book = new Epub("books_tmp/09.epub");
      console.log(this.book);
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
    }
  },
};
</script>

<style lang="scss" scoped>
#ebook {
  position: relative;

  #mask {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 100;
    display: flex;

    #left {
      flex: 0 0 20%;
    }

    #center {
      flex: 1;
    }

    #right {
      flex: 0 0 20%;
    }
  }
}
</style>