<template>
  <div class="layout-middle">
    <h1 class="text-header-left">{{ mailItem.title }}</h1>
    <p class="text-medium-left">发件人: {{ mailItem.from }}</p>
    <p class="text-medium-left">时间: {{ mailItem.date }}</p>
    <div class="auto-wrap">
      <p class="text-medium">{{ mailItem.content }} </p>
    </div>
  </div>
</template>

<script>
import "@/css/text.css";
import "@/css/layout.css";
export default{
  name: 'MailDetail',
  props: {
    mailItem: {
      type: Object,
      default: function(){
        return {from:'', title:'', date:'', content:''};
      }
    }
  },
  data(){
    return {
      // 暂时不到需要啥
    }
  }
}
</script>