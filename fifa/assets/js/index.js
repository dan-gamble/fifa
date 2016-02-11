import Vue from 'vue'
import VueResource from 'vue-resource'

import Builder from './Builder.vue'

Vue.use(VueResource)

new Vue({
  el: '#builder',
  components: {
    Builder
  }
})
