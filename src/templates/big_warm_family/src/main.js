import { createApp } from 'vue'
import App from './App.vue'

const EventHandlingApp = {
    data() {
      return {
        message: 'Hello Vue.js!'
      }
    },
    methods: {
      reverseMessage() {
        this.message = this.message
          .split('')
          .reverse()
          .join('')
      }
    }
  }
createApp(EventHandlingApp).mount('#event-handling')
createApp(App).mount('#app')
