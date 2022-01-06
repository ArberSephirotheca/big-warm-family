<script setup>
import { ref } from 'vue'

defineProps({
  msg: String
})

const count = ref(0)
</script>

<template>
  <h1>{{ msg }}</h1>

  <!--
  <p>
    Recommended IDE setup:
    <a href="https://code.visualstudio.com/" target="_blank">VSCode</a>
    +
    <a href="https://github.com/johnsoncodehk/volar" target="_blank">Volar</a>
  </p>

  <p>
    <a href="https://vitejs.dev/guide/features.html" target="_blank">
      Vite Documentation
    </a>
    |
    <a href="https://v3.vuejs.org/" target="_blank">Vue 3 Documentation</a>
  </p>
 -->
<div id="v-model-basic" class="demo">
  <p>avid: <input v-model="message" placeholder="" /> </p>
</div>

  <button type="button" @click="count++">submit</button>
  <button type="button" @click="count++">clear</button>
</template>

<style scoped>
a {
  color: #42b983;
}
</style>
