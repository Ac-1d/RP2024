<template>
  <div class="comments">
    <CommentBlock/>
  </div>
</template>

<script>
import CommentBlock from "@/components/CommentBlock.vue";
export default {
  name: "Comments",
  components: {
    CommentBlock
  }
};
</script>

<style scoped>
.comment {
  margin-bottom: 10px;
  /* 其他样式... */
}
</style>