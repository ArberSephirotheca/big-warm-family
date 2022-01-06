<template>
  <div>
    <p>{{ msg }}</p>
    <button v-on:click="reverseMessage">Reverse Message</button>
  </div>
</template>

<script>
export default {
  name: 'abc',
  data() {
    return {
      msg: 'Hello!',
    };
  },
  methods: {
    reverseMessage() {
      this.msg = 'fasdfsdf';
    },
  },
};
</script>
