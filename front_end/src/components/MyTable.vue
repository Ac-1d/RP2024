<template>
  <div v-if="rows.length>0">
    <table>
      <thead>
        <tr>
          <th v-for="(val,key,i) in rows[0]" :key = "i">{{ key }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(row, index) in rows" :key="index">
          <th v-for="(val,key,i) in row" :key = "i" >{{ val }}</th>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  props: {
    rows: Array,
  },
}
</script>