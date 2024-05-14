<template>
  <div class="reader">
    <EBook/>
    <control/>
  </div>
</template>

<script>
import EBook from "@/components/Reader/EBook.vue";

export default {
  name: "Reader",
  components: {
    EBook
  }
};
</script>
