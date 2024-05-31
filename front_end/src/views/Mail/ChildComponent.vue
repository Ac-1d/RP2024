<template>  
  <el-container>
    <el-button @click="notifyParent({index: 0, content: 'hello'})">Notify Parent</el-button>  
  </el-container>
</template>  
  
<script>  
export default {  
  methods: {  
    notifyParent(data) {  
      this.$emit('custom-event', data);  
    }  
  }  
}  
</script>