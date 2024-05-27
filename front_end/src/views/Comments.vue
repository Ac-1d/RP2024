<template>
  <div>
    <div class="comment">
      <CommentBlock :maxText=600 :myid=100 myname="李正阳"/>
      <!-- 设置数字类型要用' :attribute=value '的形式 -->
    </div>
  </div>
</template>

<script>
import CommentBlock from "@/components/CommentBlock.vue";

export default {
  name: "Comments",
  components: {
    CommentBlock,
  },
  data() {
    return {
      name: '李正阳'
    }
  }
};
</script>