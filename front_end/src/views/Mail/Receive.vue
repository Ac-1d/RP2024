<template>
  <div>
    <Mail/>
    <p>receive</p>
    <el-input 
      type="textarea" :autosize="{ minRows: 20, maxRows: 25}"></el-input>
  </div>
</template>
<script>
import Mail from '@/views/Mail/Mail.vue';
export default{
  name: 'Receive',
  components: {
    Mail
  },
}
</script>