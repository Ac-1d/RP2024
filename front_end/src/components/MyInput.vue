<template>
  <div>
    <textarea :value="value" @input="updateInput"></textarea>
    <p>剩余{{ maxLen-value.length }}</p>
    <button :disabled="exceed" type="submit">{{ name }}</button>
  </div>
</template>

<script>
export default {
  name: "MyInput",
  props: {
    // vue2,默认用value，如果不是输入框input，而是单选按钮等，需要另外处理
    value: String,
    name: String,
    maxLen: Number
  },
  data() {
    return {
      exceed: false,
    }
  },
  methods: {
    updateInput(e) {
      this.exceed = this.value.length>this.maxLen;
      this.$emit("input", e.target.value);
    },
  },
};
</script>

