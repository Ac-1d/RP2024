<template>
  <div id="table" v-if="showTable">
    <div>这里是菜单栏</div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      showTable: false
    }
  }
}
</script>