<template>  
  <el-container>  
    <ChildComponent @custom-event="handleCustomEvent" />  
    <p>{{ recieved.content }}</p>
  </el-container>  
</template>  
  
<script>  
import ChildComponent from './ChildComponent.vue';  
  
export default {  
  data() {
    return {
      recieved: {index: 1, content: 'aaa'}
    }
  },
  components: {  
    ChildComponent  
  },  
  methods: {  
    handleCustomEvent(data) {  
      console.log('Received data from child:', data);  
      this.recieved = data;
      // 在这里处理从子组件传来的数据或执行相应的方法  
    }  
  }  
}  
</script>