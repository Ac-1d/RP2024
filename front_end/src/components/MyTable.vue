<template>
  <div v-if="rows.length>0">
    <table>
      <tr>
        <th v-for="(val,key,i) in rows[0]" :key = "i">{{ key }}</th>
      </tr>
      <tr v-for="(row, index) in rows" :key="index">
        <td v-for="(val,key,i) in row" :key = "i">{{ val }}</td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  props: {
    rows: Array
  }
}
</script>

<style>
table{
  width: 100px;
  text-align: left;
  font-weight: bold;
  th{
    border-radius: 4px;
    height: 50px;
    background-color: grey;
    color: white;
  }
  td{
    height: 50px;
  }
}
</style>