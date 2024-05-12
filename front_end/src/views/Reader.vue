<template>
  <div ref="viewer"></div>
</template>

<script>
import ePub from 'epubjs';

export default {
  mounted() {
    this.loadEpub();
  },
  methods: {
    loadEpub() {
      const viewer = this.$refs.viewer;
      const book = ePub("@/books_tmp/09.epub");

      book.renderTo(viewer, {
        width: "100%",
        height: "100%"
      });
    }
  }
};
</script>
