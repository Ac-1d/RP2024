<template>
  <div v-if="rows.length>0">
    <table>
      <tr>
        <th v-for="(val,key,i) in rows[0]" :key = "i" :id="key">{{ key }}</th>
      </tr>
      <tr v-for="(row, index) in rows" :key="index">
        <td v-for="(val,key,i) in row" :key = "i" :id="key">{{ val }}</td>
      </tr>
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