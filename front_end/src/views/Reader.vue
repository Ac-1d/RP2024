<template>
  <div class="reader">
    <EBook/>
  </div>
</template>

<script>
import EBook from "@/components/EBook.vue";

export default {
  name: "Reader",
  props: [
    'showNav'
  ],
  components: {
    EBook
  }
};
</script>
