<template>
  <div>
    <div class="comment">
      <CommentBlock :maxText=600 :myid=100 myname="李正阳"/>
      <!-- 设置数字类型要用' :attribute=value '的形式 -->
    </div>
    <div class="message">
      <MessageBlock />
    </div>
  </div>
</template>

<script>
import CommentBlock from "@/components/CommentBlock.vue";
import MessageBlock from "@/components/MessageBlock.vue";

export default {
  name: "Comments",
  components: {
    CommentBlock,
    MessageBlock
  },
  data() {
    return {
      name: '李正阳'
    }
  }
};
</script>

<style scoped>
.comment {
  margin-bottom: 10px;
  width: 200px;
  float: left;
  background-color: rgb(0, 200, 255);
  /* 其他样式... */
}
.message {
  margin-bottom: 10px;
  width: 300px;
  float: right;
  background-color: rgb(150, 255, 0);
}
</style>