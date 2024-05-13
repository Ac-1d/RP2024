<template>
  <div class="reader">
    <div class="reader-test">
      <div id="read">阅读器在这</div>
      <div>阅读器不在这</div>
    </div>
  </div>
</template>

<script>
import Epub from "epubjs";

export default {
  mounted() {
    this.loadEpub();
  },
  methods: {
    loadEpub() {
      this.book = new Epub("books_tmp/09.epub");
      console.log(this.book);
      this.rendition = this.book.renderTo("read", {
        width: window.innerWidth,
        height: window.innerHeight
      });
      this.rendition.display();
    }
  }
};
</script>
