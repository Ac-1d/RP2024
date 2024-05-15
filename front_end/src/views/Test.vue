<template>
  <div id="app">
    <p>{{ message }}</p>
    <div>
      <router-link to="/comments">Comments</router-link>
    </div>
    <router-view />
  </div>
</template>

<script>
export default {
  data(){
    return {
      'message': 'hello',
      'name': 'Lzy'
    }
  }
}
</script>